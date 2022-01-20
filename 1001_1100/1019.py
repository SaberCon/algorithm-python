# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []
        i = 0
        while head:
            val = head.val
            while stack and stack[-1][1] < val:
                ans[stack.pop()[0]] = val
            ans.append(0)
            stack.append((i, val))
            i += 1
            head = head.next
        return ans
