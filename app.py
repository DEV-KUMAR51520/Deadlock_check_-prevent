from flask import Flask, render_template, jsonify, request
from bankes import Bankers
from detection import DeadlockDetector
from recovery import Recovery

app = Flask(__name__)

# ----------------------
#  Default UI Route
# ----------------------
@app.route("/")
def index():
    return render_template("index.html")

# ----------------------
#  API Routes
# ----------------------
state = {
    'available': [3, 3, 2],
    'max': [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ],
    'allocation': [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
}

@app.route("/state")
def get_state():
    return jsonify(state)

@app.route("/is_safe")
def is_safe():
    b = Bankers(state["available"], state["max"], state["allocation"])
    safe, seq = b.is_safe()
    return jsonify({"safe": safe, "sequence": seq})

@app.route("/request", methods=["POST"])
def request_resources():
    data = request.json
    pid = int(data["pid"])
    req = list(map(int, data["request"]))
    b = Bankers(state["available"], state["max"], state["allocation"])
    granted, msg = b.request_resources(pid, req)

    if granted:
        state["available"] = b.available
        state["allocation"] = b.allocation

    return jsonify({"granted": granted, "message": msg, "state": state})

@app.route("/detect_deadlock")
def detect_deadlock():
    alloc = state["allocation"]
    maxd = state["max"]
    n = len(alloc)
    m = len(alloc[0])
    need = [[maxd[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    req_matrix = [[1 if need[i][j] > 0 else 0 for j in range(m)] for i in range(n)]

    d = DeadlockDetector(alloc, req_matrix)
    cycles = d.detect_deadlocks()

    return jsonify({"cycles": cycles})

@app.route("/recover", methods=["POST"])
def recover():
    data = request.json
    policy = data.get("policy", "lowest_alloc")

    alloc = state["allocation"]
    maxd = state["max"]
    m = len(maxd[0])
    n = len(alloc)

    need = [[maxd[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    killed = Recovery.kill_processes(policy, alloc, need, state["available"])

    return jsonify({"killed": killed, "state": state})

@app.route('/graph', methods=['GET'])
def graph():
    n = len(state['allocation'])
    m = len(state['available'])
    nodes = []
    edges = []

    # Process nodes
    for i in range(n):
        nodes.append({'id': f'P{i}', 'type': 'process'})

    # Resource nodes
    for j in range(m):
        nodes.append({'id': f'R{j}', 'type': 'resource', 'available': state['available'][j]})

    # Need matrix
    need = [[state['max'][i][j] - state['allocation'][i][j] for j in range(m)] for i in range(n)]

    # Allocation edges (R → P)
    for i in range(n):
        for j in range(m):
            if state['allocation'][i][j] > 0:
                edges.append({
                    'source': f'R{j}',
                    'target': f'P{i}',
                    'type': 'allocation',
                    'weight': state['allocation'][i][j]
                })

    # Request edges (P → R)
    for i in range(n):
        for j in range(m):
            if need[i][j] > 0:
                edges.append({
                    'source': f'P{i}',
                    'target': f'R{j}',
                    'type': 'request',
                    'weight': need[i][j]
                })

    return jsonify({'nodes': nodes, 'edges': edges, 'need': need})

if __name__ == "__main__":
    app.run(debug=True)
