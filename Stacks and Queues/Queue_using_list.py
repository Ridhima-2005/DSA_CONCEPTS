# Implement QUEUE using List:-
'''
QUEUE:- Data structure that can store any type of data like int,float, list and complex data like objects.

---> Works on FIFO mechanism.
---> Operations can be performed from both the ends called rear and front.
By default, 
Rear end---> generally used for insertion of elements
Front end---> generally used for deletion of elements

Queue Operations:
Enqueue()  ---> Insertion using append()
Dequeue()   ---> Deletion using pop()
Front()  ---> Print the first element using [0] index
Rear()  ---> Print the last element using [-1] index
'''

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if len(self.items) == 0:
            return "Cannot pop! Queue is empty"
        x = self.items.pop(0)
        return x
    def front(self):
        if len(self.items) == 0:
            return "Queue is empty"
        return self.items[0]
    def rear(self):
        if len(self.items) == 0:
            return "Queue is empty"
        return self.items[-1]
    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(50)
queue.enqueue(100)
queue.enqueue(150)
queue.enqueue(200)
queue.enqueue(250)
print(f"Queue content = {queue.items}")
print(f"Popped item  = {queue.dequeue()}")
print(f"Queue content = {queue.items}")
print(f"First element after pop = {queue.front()}")
print(f"Last element after pop = {queue.rear()}")
print(f"Queue is empty = {queue.is_empty()}")