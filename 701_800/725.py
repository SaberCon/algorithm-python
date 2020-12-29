# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        size = 0
        node = root
        while node:
            size += 1
            node = node.next
        rest = size % k
        ans = []
        for _ in range(k):
            ans.append(root)
            for _ in range(size // k if rest else (size // k - 1)):
                root = root.next
            if rest:
                rest -= 1
            if root:
                temp = root.next
                root.next = None
                root = temp
        return ans
