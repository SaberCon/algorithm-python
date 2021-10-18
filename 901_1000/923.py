from collections import Counter


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr)
        nums = sorted((k, v) for k, v in counter.items())
        ans = 0
        for i, (num, count) in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if num + nums[left][0] + nums[right][0] < target:
                    left += 1
                elif num + nums[left][0] + nums[right][0] > target:
                    right -= 1
                else:
                    ans += count * nums[left][1] * nums[right][1]
                    left += 1
                    right -= 1
            if num * 3 == target:
                ans += count * (count - 1) * (count - 2) // 6
            if target - num * 2 > num and target - num * 2 in counter:
                ans += (count * (count - 1) // 2) * counter[target - num * 2]
            if (target - num) % 2 == 0 and (target - num) // 2 > num and (target - num) // 2 in counter:
                ans += count * counter[(target - num) // 2] * (counter[(target - num) // 2] - 1) // 2
        return ans % (10 ** 9 + 7)
