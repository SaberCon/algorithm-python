class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def key(log):
            log = log.split()
            if log[1].isdigit():
                return '{', '}'
            return ' '.join(log[1:]), log[0]

        return sorted(logs, key=key)
