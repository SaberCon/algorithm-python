# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        nodes = [ListNode(next=head)]
        while head:
            total = 0
            for i in range(len(nodes) - 1, -1, -1):
                if total + head.val == 0:
                    nodes = nodes[:i + 1]
                    nodes[-1].next = head.next
                    break
                total += nodes[i].val
            else:
                nodes.append(head)
            head = head.next
        return nodes[0].next
