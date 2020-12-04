class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task_counts = {}
        for task in tasks:
            task_counts[task] = task_counts.get(task, 0) + 1
        counts = sorted(task_counts.values(), reverse=True)
        ans = 0
        while counts:
            curr_len = len(counts)
            for i in range(min(curr_len, n + 1)):
                counts[i] -= 1
            counts = sorted(filter(lambda c: c > 0, counts), reverse=True)
            ans += n + 1 if counts else curr_len
        return ans
