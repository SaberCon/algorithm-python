# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        ans = 0
        while head:
            if head.val in G and getattr(head.next, 'val', None) not in G:
                ans += 1
            head = head.next
        return ans
