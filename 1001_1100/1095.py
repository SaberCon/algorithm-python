# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find(left_index, left, right_index, right, monotone):
            if right_index - left_index < 2:
                return right_index if right == target else -1
            mid_index = (left_index + right_index) // 2
            mid = mountain_arr.get(mid_index)
            if mid > left and mid > right:
                if target > left:
                    ans = find(left_index, left, mid_index, mid, False)
                    if ans >= 0:
                        return ans
                if target >= right:
                    ans = find(mid_index, mid, right_index, right, False)
                    if ans >= 0:
                        return ans
                return -1
            if target == mid:
                return mid_index
            if monotone:
                if left < target < mid or mid < target < left:
                    return find(left_index, left, mid_index, mid, True)
                if right < target < mid or mid < target < right:
                    return find(mid_index, mid, right_index, right, True)
                return -1
            if left < right:
                if target < mid:
                    return find(left_index, left, mid_index, mid, True)
                return find(mid_index, mid, right_index, right, False)
            if target == right:
                return right_index
            if target < mid:
                return find(mid_index, mid, right_index, right, True)
            return find(left_index, left, mid_index, mid, False)

        n = mountain_arr.length()
        left_value, right_value = mountain_arr.get(0), mountain_arr.get(n - 1)
        if target == left_value:
            return 0
        return find(0, left_value, n - 1, right_value, False)
