class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((left, index) for index, (left, right) in enumerate(intervals))

        def get_right_interval(min_value, start, end):
            if start == end:
                return starts[start][1] if starts[start][0] >= min_value else -1
            mid = (start + end) // 2
            if starts[mid][0] >= min_value:
                return get_right_interval(min_value, start, mid)
            else:
                return get_right_interval(min_value, mid + 1, end)

        return [get_right_interval(right, 0, len(starts) - 1) for left, right in intervals]
