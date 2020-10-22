class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        def dfs(prev, curr):
            if not curr:
                return prev
            prev.next = curr
            curr.prev = prev
            next = curr.next
            tail = dfs(curr, curr.child)
            curr.child = None
            return dfs(tail, next)

        dfs(Node(None, None, None, None), head)
        head.prev = None
        return head
