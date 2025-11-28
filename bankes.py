# bankes.py
class Bankers:
    def __init__(self, available, maximum, allocation):
        self.available = available
        self.maximum = maximum
        self.allocation = allocation
        self.need = [[self.maximum[i][j] - self.allocation[i][j]
                      for j in range(len(self.available))]
                     for i in range(len(self.maximum))]

    def is_safe(self):
        work = self.available.copy()
        finish = [False] * len(self.maximum)
        safe_sequence = []

        while True:
            found = False
            for i in range(len(self.maximum)):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(len(work))):
                    for j in range(len(work)):
                        work[j] += self.allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(i)
                    found = True
            if not found:
                break

        return (all(finish), safe_sequence)

    def request_resources(self, process_id, request):
        if any(request[j] > self.need[process_id][j] for j in range(len(request))):
            return False, "Request exceeds need"

        if any(request[j] > self.available[j] for j in range(len(request))):
            return False, "Request exceeds available"

        prev_avail = self.available.copy()
        prev_alloc = [row.copy() for row in self.allocation]
        prev_need = [row.copy() for row in self.need]

        for j in range(len(request)):
            self.available[j] -= request[j]
            self.allocation[process_id][j] += request[j]
            self.need[process_id][j] -= request[j]

        safe, _ = self.is_safe()

        if safe:
            return True, "Request granted"
        else:
            self.available = prev_avail
            self.allocation = prev_alloc
            self.need = prev_need
            return False, "Request leads to unsafe state"
