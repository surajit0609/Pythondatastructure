class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None
    def is_empty(self):
        return self.front==None
    def enqueue(self,item):
        temp=Node(item)
        if self.rear==None:
            self.front=self.rear=temp
            return
        else:
            self.rear.next=temp
            self.rear=temp
    def dequeue(self):
        if self.is_empty():
            return
        temp=self.front
        self.front=temp.next
        if self.front==None:
            self.rear=None

q1=Queue()
q1.enqueue(34)
q1.enqueue(54)
q1.dequeue()

            
        
        