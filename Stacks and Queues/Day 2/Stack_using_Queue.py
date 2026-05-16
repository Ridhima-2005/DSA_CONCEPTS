# Implementation of STACK using QUEUE

from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self,item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if (len(self.queue)==0):
            return "Stack is empty"
        return self.queue.popleft()
    
    def peek(self):
        if (len(self.queue)==0):
            return "Stack is empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
stack = StackUsingQueue()

stack.push(100)
stack.push(200)
stack.push(300)
stack.push(400)

print(f"Stack content = {stack.queue}")
print(f"Top element: {stack.peek()}")
print(f"Popped element: {stack.pop()}")
print(f"Top element after pop: {stack.peek()}")
print(f"Stack content = {stack.queue}")