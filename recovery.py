# recovery.py
class Recovery:
    @staticmethod
    def kill_processes(strategy, allocation, need, available):
        if strategy == "lowest_alloc":
            alloc_sum = [sum(a) for a in allocation]
            victim = alloc_sum.index(min(alloc_sum))
            return [victim]

        elif strategy == "highest_need":
            need_sum = [sum(n) for n in need]
            victim = need_sum.index(max(need_sum))
            return [victim]

        return []
