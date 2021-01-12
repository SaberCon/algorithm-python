import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        counts = [(-count, char) for char, count in Counter(S).items()]
        heapq.heapify(counts)
        ans = ''
        while counts:
            count, char = heapq.heappop(counts)
            if ans and char == ans[-1]:
                if not counts:
                    return ''
                count2, char2 = heapq.heappop(counts)
                ans += char2
                heapq.heappush(counts, (count, char))
                if count2 < -1:
                    heapq.heappush(counts, (count2 + 1, char2))
            else:
                ans += char
                if count < -1:
                    heapq.heappush(counts, (count + 1, char))
        return ans
