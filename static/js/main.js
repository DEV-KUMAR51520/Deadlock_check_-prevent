function print(msg) {
    document.getElementById("outputBox").textContent = JSON.stringify(msg, null, 2);
}

function loadState() {
    api.loadState().then(print);
}

function checkSafety() {
    api.checkSafe().then(print);
}

function sendRequest() {
    let pid = parseInt(document.getElementById("pid").value);
    let req = document.getElementById("req").value.split(",").map(Number);
    api.request(pid, req).then(print);
}

function releaseResources() {
    let pid = parseInt(document.getElementById("relPid").value);
    let rel = document.getElementById("relVec").value.split(",").map(Number);
    api.release(pid, rel).then(print);
}

function runDeadlock() {
    api.detectDeadlock().then(print);
}

function recover() {
    let policy = document.getElementById("policySelect").value;
    api.recover(policy).then(print);
}

function autoDeadlock() {
    print("⚠️ Creating Deadlock Scenario...");
    api.request(0, [1,0,0]).then(() => {
        api.request(1, [0,1,0]).then(() => {
            api.request(2, [0,0,1]).then(() => {
                runDeadlock();
                renderGraph();
            });
        });
    });
}
