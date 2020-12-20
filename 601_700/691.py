import collections


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        t_count = collections.Counter(target)
        s_counts = [collections.Counter(sticker) & t_count for sticker in stickers]
        for state in range(len(s_counts) - 1, -1, -1):
            if any(s_counts[state] & s_counts[j] == s_counts[state] for j in range(len(s_counts)) if state != j):
                s_counts.pop(state)
        n, states = len(target), (1 << len(target)) - 1
        dp = [0] + [16] * states
        for state in range(states):
            if dp[state] > 15:
                continue
            for s_count in s_counts:
                next_state = state
                remained = s_count.copy()
                for i in range(n):
                    if state & (1 << i) == 0 and remained[target[i]] > 0:
                        next_state |= (1 << i)
                        remained[target[i]] -= 1
                dp[next_state] = min(dp[next_state], dp[state] + 1)
        return -1 if dp[-1] > 15 else dp[-1]
