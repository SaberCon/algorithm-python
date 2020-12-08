class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = [0] * k
        self.empty = True
        self.start = self.end = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.start = self._get_last_pos(self.start)
        self.deque[self.start] = value
        self.empty = False
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.deque[self.end] = value
        self.end = self._get_next_pos(self.end)
        self.empty = False
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.start = self._get_next_pos(self.start)
        if self.isFull():
            self.empty = True
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.end = self._get_last_pos(self.end)
        if self.isFull():
            self.empty = True
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.deque[self.start]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.deque[self._get_last_pos(self.end)]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.empty

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return not self.empty and self.start == self.end

    def _get_next_pos(self, curr: int) -> int:
        return (curr + 1) % len(self.deque)

    def _get_last_pos(self, curr: int) -> int:
        return (curr - 1 + len(self.deque)) % len(self.deque)
