from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()


contracts = Stack()
contracts.push("A")
contracts.push("B")
contracts.push("C")
print(contracts.pop())

print(contracts.stack)
contracts.stack.rotate()
print(contracts.stack)
contracts.stack.remove("A")
print(contracts.stack)
print(contracts.stack.count("A"))
