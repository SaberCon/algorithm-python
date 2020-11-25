class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        num_set = set()
        duplicates = set()
        for num in nums:
            if num in num_set:
                duplicates.add(num)
            else:
                num_set.add(num)
        if k == 0:
            return len(duplicates)
        sorted_num = sorted(num_set)
        i = 0
        for num in sorted_num:
            while sorted_num[i] + k < num:
                i += 1
            if sorted_num[i] + k == num:
                ans += 1
        return ans
