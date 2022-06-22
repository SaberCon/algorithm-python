from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # 0-closed 1-open 2-seen 3-used
        open_boxes = []
        for box in initialBoxes:
            if status[box]:
                status[box] = 3
                open_boxes.append(box)
            else:
                status[box] = 2
        ans = 0
        while open_boxes:
            box = open_boxes.pop()
            ans += candies[box]
            for k in keys[box]:
                if status[k] == 0:
                    status[k] = 1
                if status[k] == 2:
                    status[k] = 3
                    open_boxes.append(k)
            for b in containedBoxes[box]:
                if status[b] == 0:
                    status[b] = 2
                if status[b] == 1:
                    status[b] = 3
                    open_boxes.append(b)
        return ans
