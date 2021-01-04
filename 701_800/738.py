class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        nums = str(N)
        ans = ['0']
        for n in nums:
            if n < ans[-1]:
                d = str(int(ans[-1]) - 1)
                while ans[-1] > d:
                    ans.pop()
                ans.append(d)
                break
            ans.append(n)
        return int(''.join(ans).ljust(len(nums) + 1, '9'))
