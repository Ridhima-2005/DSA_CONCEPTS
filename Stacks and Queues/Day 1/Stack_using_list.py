# Implement STACK using List:-
'''
STACK:- Data structure that can store any type of data like int,float and complex data like objects.

---> Works on LIFO mechanism.
---> Operations can be performed by one end only called top.

Stack Operations:
Push()  ---> Insertion using append()
Pop()   ---> Deletion using pop()
Peek()  ---> Print the top element using [-1] index
'''
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            return "Cannot pop! Stack is empty"
        x = self.items.pop()
        return x
    def peek(self):
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items[-1]
    def size(self):
        return len(self.items)

stack = Stack()
stack.push(5)
stack.push(100)
stack.push(15)
print(f"Stack content = {stack.items}")
print(f"Popped item  = {stack.pop()}")
print(f"Stack content = {stack.items}")
print(f"Top element after pop = {stack.peek()}")
print(f"Stack is empty = {stack.is_empty()}")