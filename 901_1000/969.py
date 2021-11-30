class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        N = len(arr)
        ans = []
        for i in sorted(range(N), key=lambda i: -arr[i]):
            for a in ans:
                if i < a:
                    i = a - i - 1
            ans.extend((i + 1, N - len(ans) // 2))
        return ans
