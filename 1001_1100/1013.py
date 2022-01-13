class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3:
            return False
        target = total // 3
        current = 0
        parts = 0
        for num in arr[:-1]:
            current += num
            if current == target:
                current = 0
                parts += 1
            if parts == 2:
                return True
        return False
