class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        if (rec1[0], rec1[1]) > (rec2[0], rec2[1]):
            rec1, rec2 = rec2, rec1
        if rec1[1] <= rec2[1]:
            return rec1[2] > rec2[0] and rec1[3] > rec2[1]
        return rec1[2] > rec2[0] and rec1[1] < rec2[3]
