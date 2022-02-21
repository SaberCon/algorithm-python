class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                index, num = i + 1, arr[i + 1]
                for j in range(i + 2, len(arr)):
                    if arr[i] <= arr[j]:
                        break
                    if arr[j] > num:
                        index, num = j, arr[j]
                arr[i], arr[index] = arr[index], arr[i]
                break
        return arr
