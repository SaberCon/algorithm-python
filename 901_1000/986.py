class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        f_i = s_i = 0
        while f_i < len(firstList) and s_i < len(secondList):
            f_start, f_end = firstList[f_i]
            s_start, s_end = secondList[s_i]
            intersection = [max(f_start, s_start), min(f_end, s_end)]
            if intersection[0] <= intersection[1]:
                ans.append(intersection)
            if f_end < s_end:
                f_i += 1
            else:
                s_i += 1
        return ans
