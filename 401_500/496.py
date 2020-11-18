class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_map = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                greater_map[stack.pop()] = num
            stack.append(num)
        return [greater_map.get(num, -1) for num in nums1]
