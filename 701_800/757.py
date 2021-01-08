class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: (i[0], -i[1]))
        key_intervals = []
        for start, end in intervals:
            while key_intervals and key_intervals[-1][1] >= end:
                key_intervals.pop()
            key_intervals.append([start, end, 0])
        ans = 0
        for i, (start, end, count) in enumerate(key_intervals):
            if count > 1:
                continue
            for _ in range(count, 2):
                for j in range(i, len(key_intervals)):
                    if key_intervals[j][0] > end:
                        break
                    key_intervals[j][2] += 1
                end -= 1
            ans += 2 - count
        return ans
