class Solution:
    def __init__(self):
        self.cache = {}
        self.sub = [0]

    def splitArray(self, nums: List[int], m: int) -> int:
        for elem in nums:
            self.sub.append(self.sub[-1] + elem)
        return self.split_array(0, len(nums), m)

    def split_array(self, start: int, end: int, count: int) -> int:
        if (start, end, count) in self.cache:
            return self.cache[(start, end, count)]
        if count == 1:
            ans = self.sub[end] - self.sub[start]
        else:
            ans = 10 ** 9
            for i in range(start + 1, end - count + 2):
                left = self.split_array(start, i, 1)
                right = self.split_array(i, end, count - 1)
                ans = min(ans, max(left, right))
                if left >= right:
                    break
        self.cache[(start, end, count)] = ans
        return ans
