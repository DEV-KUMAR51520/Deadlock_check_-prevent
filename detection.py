# detection.py
class DeadlockDetector:
    def __init__(self, allocation, request):
        self.allocation = allocation
        self.request = request
        self.process_count = len(allocation)
        self.resource_count = len(allocation[0])

    def detect_deadlocks(self):
        graph = {}

        for p in range(self.process_count):
            for r in range(self.resource_count):
                if self.request[p][r] == 1:
                    graph[f"P{p}"] = graph.get(f"P{p}", []) + [f"R{r}"]

        for p in range(self.process_count):
            for r in range(self.resource_count):
                if self.allocation[p][r] == 1:
                    graph[f"R{r}"] = graph.get(f"R{r}", []) + [f"P{p}"]

        visited = set()
        stack = set()
        cycles = []

        def dfs(node, path):
            visited.add(node)
            stack.add(node)
            path.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, path)
                elif neighbor in stack:
                    cycle_start = path.index(neighbor)
                    cycles.append(path[cycle_start:].copy())

            path.pop()
            stack.remove(node)

        for node in graph:
            if node not in visited:
                dfs(node, [])

        return cycles
