class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2 = [], []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while list1 or list2 or carry:
            curr = (list1.pop() if list1 else 0) + (list2.pop() if list2 else 0) + carry
            node = ListNode(curr % 10)
            node.next = ans
            ans = node
            carry = curr // 10
        return ans
