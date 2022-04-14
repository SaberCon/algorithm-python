# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        sum_node = {}

        total = 0
        node = dummy
        while node:
            total += node.val
            sum_node[total] = node
            node = node.next

        total = 0
        node = dummy
        while node:
            total += node.val
            if total in sum_node:
                node.next = sum_node[total].next
            node = node.next

        return dummy.next
