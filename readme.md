# Deadlock Detection & Banker's Algorithm Simulator

A complete interactive toolkit for:

- **Banker’s Algorithm**  
- **Deadlock Detection** using a Resource Allocation Graph  
- **Deadlock Recovery** using custom policies  
- **Visual Simulation** with D3.js (process-resource graph)  
- **Backend REST API** built using Flask  
- **Full Test Suite** using pytest  

This project is designed for OS practicals, university submissions, and learning deadlock algorithms interactively.

---

# 📁 Project Structure

deadlock/
│── app.py # Flask server (API + UI backend)
│── bankes.py # Banker's Algorithm implementation
│── detection.py # Deadlock graph cycle detection
│── recovery.py # Deadlock recovery handler
│── requirements.txt # Dependencies
│── README.md # Documentation
│── venv/ (ignored) # Virtual environment
│
├── tests/
│ ├── test_bankers.py
│ ├── test_detection.py
│ └── test_recovery.py
│
└── static/
└── index.html # Frontend visualization (D3.js)


---

# 🚀 Setup Instructions (For Anyone Cloning This Repository)

Below are the **exact steps a new user should follow** after cloning your repo.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Create a Python virtual environment
python -m venv venv

3️⃣ Activate the virtual environment
Windows PowerShell
.\venv\Scripts\activate

Windows CMD
venv\Scripts\activate.bat

Linux / macOS
source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Run the test suite (recommended)
python -m pytest -q
Expected output:
3 passed in X.XXs

6️⃣ Run the application
python app.py
The app will start on:
http://127.0.0.1:5000
🧪 API Endpoints Documentation (Testing Guide)
This explains every API endpoint with example requests.
You can test all of these using:
Postman
Thunder Client
curl

Browser (for GET routes)

1. GET /state
Returns the current state of the simulation.

Example:
GET http://127.0.0.1:5000/state
2. GET /is_safe
Runs Banker's Algorithm — checks whether the system is in a safe state.

Example:
GET http://127.0.0.1:5000/is_safe
Sample Response:
{
  "safe": true,
  "safe_sequence": [1,0,3,4,2]
}
3. POST /request
Request additional resources for a process.

JSON Body:
{
  "pid": 1,
  "request": [1,0,2]
}
Example:
POST http://127.0.0.1:5000/request
4. POST /release
Release resources previously allocated to a process.

JSON Body:
{
  "pid": 0,
  "release": [0,1,0]
}
5. GET /graph
Returns graph data for the D3 visualizer.

Example:
GET http://127.0.0.1:5000/graph
6. GET /detect_deadlock
Detects cycles in the resource allocation graph.

Example:
GET http://127.0.0.1:5000/detect_deadlock
Example Response:
{
  "deadlock_cycles": [
    ["P0", "R0", "P1", "R1"]
  ]
}
7. POST /recover
Triggers deadlock recovery using a policy.

JSON Body:
{
  "policy": "lowest_alloc"
}
Example:
POST http://127.0.0.1:5000/recover
Example Response:
{
  "killed": [2],
  "state": {...}
}
🧬 Algorithms Implemented
🔹 Banker's Algorithm


Safety check
Need matrix calculation
Request validation
state simulation

🔹 Deadlock Detection
Builds a Resource Allocation Graph (RAG)

Uses networkx.simple_cycles() for cycle detection

🔹 Deadlock Recovery
Current policy: lowest_alloc (kills process with least allocated resources)

You can add more strategies easily

🧪 Running Tests
To ensure everything works:

python -m pytest -q
Tests include:

Safety algorithm verification

Resource request granting/denying

Deadlock cycle detection

Recovery mechanism

🖥️ Using the Frontend (D3 Graph Visualizer)
Open:

http://127.0.0.1:5000/
You get:

Dynamic graph of processes (P0…Pn)

Resource nodes (R0…Rm)

Request and allocation edges

Live updates after requests / releases

📦 Deploying This Project
Option A — Default
python app.py
Option B — Production (Windows recommended)
pip install waitress
waitress-serve --call "app:create_app"
📘 For Developers / Contributors
Adding New Features
New algorithms can be added under:

bankes.py

detection.py

recovery.py

Adding Test Cases
Place new test files inside:

tests/