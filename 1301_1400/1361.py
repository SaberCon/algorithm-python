from collections import deque
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        seen = set(range(n)) - set(leftChild) - set(rightChild)
        if len(seen) != 1:
            return False
        queue = deque(seen)
        leafs = 0
        while queue:
            node = queue.popleft()
            for child in (leftChild[node], rightChild[node]):
                if child == -1:
                    leafs += 1
                    continue
                if child in seen:
                    return False
                seen.add(child)
                queue.append(child)
        return leafs == n + 1 and len(seen) == n
