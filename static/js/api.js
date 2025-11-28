const api = {

    loadState: () => fetch("/state").then(res => res.json()),

    checkSafe: () => fetch("/is_safe").then(res => res.json()),

    request: (pid, req) =>
        fetch("/request", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ pid, request: req })
        }).then(res => res.json()),

    release: (pid, rel) =>
        fetch("/release", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ pid, release: rel })
        }).then(res => res.json()),

    detectDeadlock: () => fetch("/detect_deadlock").then(res => res.json()),

    recover: (policy) =>
        fetch("/recover", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ policy })
        }).then(res => res.json()),

    graphData: () => fetch("/graph").then(res => res.json()),
};
