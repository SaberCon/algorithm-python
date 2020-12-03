class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0] * k
        self.empty = True
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear += 1
        if self.rear == len(self.queue):
            self.rear = 0
        self.empty = False
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front += 1
        if self.front == len(self.queue):
            self.front = 0
        if self.front == self.rear:
            self.empty = True
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.empty

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return not self.queue or (not self.empty and self.front == self.rear)
