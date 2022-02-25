class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        N = max(len(arr1), len(arr2))
        arr1 = arr1[::-1] + [0] * (N - len(arr1))
        arr2 = arr2[::-1] + [0] * (N - len(arr2))
        ans = [0] * (N + 2)
        for i, (n1, n2) in enumerate(zip(arr1, arr2)):
            ans[i] += n1 + n2
            if ans[i] > 1:
                ans[i] -= 2
                if ans[i + 1] > 0:
                    ans[i + 1] -= 1
                else:
                    ans[i + 1] += 1
                    ans[i + 2] += 1
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        return ans[::-1]
