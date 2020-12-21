class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        part = total // k
        nums.sort(reverse=True)
        dp = {(part,) * k}
        for num in nums:
            new_dp = set()
            for state in dp:
                for i in range(k):
                    if state[i] >= num:
                        new_dp.add(state[:i] + (state[i] - num,) + state[i + 1:])
                    if state[i] == part:
                        break
            dp = new_dp
        return (0,) * k in dp
