class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * self.size
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                # if empty, point front at 0
                self.front = 0
            # circularly increase rear and set value at rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                # that is if it is the last element
                self.front = self.rear = -1
            else:
                # otherwise just keep incrementing the front circularly
                self.front = (self.front + 1) % self.size
            return True
        else:
            return False

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear == -1

    def isFull(self) -> bool:
        # if the next value after rear is front queue full
        return ((self.rear + 1) % self.size)  == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()