from collections import deque


class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, elem):
        self.data.append(elem)

    def dequeue(self):
        if len(self.data) == 0:
            return None
        else:
            return self.data.popleft()

    def __str__(self):
        return ", ".join(self.data)

    def __len__(self):
        return len(self.data)

