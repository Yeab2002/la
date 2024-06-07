class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.head = self.tail = -1
        self.max_size = k

    def enqueue(self, value):
        if (self.tail + 1) % self.max_size == self.head:
            return False  # Queue is full
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = value
        return True

    def dequeue(self):
        if self.head == -1:
            return None  # Queue is empty
        result = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1  # Queue is now empty
        else:
            self.head = (self.head + 1) % self.max_size
        return result

    def front(self):
        if self.head == -1:
            return None  # Queue is empty
        return self.queue[self.head]

    def rear(self):
        if self.tail == -1:
            return None  # Queue is empty
        return self.queue[self.tail]

    def is_empty(self):
        return self.head == -1

# Test CircularQueue
cq = CircularQueue(3)
print("Enqueue operations:")
print(cq.enqueue(1))  # Output: True
print(cq.enqueue(2))  # Output: True
print(cq.enqueue(3))  # Output: True
print(cq.enqueue(4))  # Output: False (queue is full)
print("Dequeue operation:", cq.dequeue())  # Output: 1
print("Enqueue operation:", cq.enqueue(4))  # Output: True
print("Front of queue:", cq.front())  # Output: 2
print("Rear of queue:", cq.rear())  # Output: 4
