class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted((num, 1) for num in arr)
        for i, (num, count) in enumerate(sorted_arr):
            if i > 0 and sorted_arr[i - 1][0] == num:
                sorted_arr[i] = (num, sorted_arr[i - 1][1] + 1)
        top = (0, 0)
        ans = 0
        for i, num in enumerate(arr):
            if num == top[0]:
                top = (num, top[1] + 1)
            if num > top[0]:
                top = (num, 1)
            if top == sorted_arr[i]:
                ans += 1
        return ans
