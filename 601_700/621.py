class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task_counts = {}
        for task in tasks:
            task_counts[task] = task_counts.get(task, 0) + 1
        counts = sorted(task_counts.values())
        top = counts.pop() - 1
        idles = top * n
        while idles > 0 and counts:
            idles -= min(top, counts.pop())
        return len(tasks) + max(idles, 0)
