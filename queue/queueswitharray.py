class Queues:
    def __init__(self,limit):
        self.element=[]
        self.limit=limit
    def enqueue(self,data):
        if self.limit==len(self.element):
            print("overflow")
            return 
        self.element.append(data)
    def dequeue(self):
        self.element.pop(0)
    def rear(self):
        return self.element[-1]
    def front(self):
        return self.element[0]
    def isempty(self):
        return len(self.element)==0
    def display(self):
        return self.element

Q=Queues(5)
Q.enqueue(67)
Q.enqueue(68)
Q.enqueue(69)
Q.enqueue(70)
Q.enqueue(71)
Q.enqueue(72)
print(Q.isempty())
print(Q.rear())
print(Q.front())
print(Q.display())
Q.dequeue()
Q.dequeue()
print(Q.isempty())
print(Q.rear())
print(Q.front())
print(Q.display())
        