class Queue:
    def __init__(self,limit):
        self.capacity=limit
        self.front=-1
        self.rear=-1
        self.q=[0]*limit
    def is_empty(self):
        if self.front == -1 and self.rear== -1:
            return True
        else:
            return False
    def is_full(self):
        if (self.rear+1)%self.capacity==self.front:
            return True
        else:
            return False
        
    def enqueue(self,data):
        if self.is_full():
            print("overfalow")
            return 
        if self.is_empty():
            self.front=(self.front+1)%self.capacity
            self.rear=(self.rear+1)%self.capacity
            self.q[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.capacity
            self.q[self.rear]=data
    def dequeue(self):
        if self.is_empty():
            print('underfalow')
            return 
        if self.front==self.rear:
            self.q[self.front]=0
            self.front=self.rear=-1
        else:
            self.q[self.front]=0
            self.front=(self.front+1)%self.capacity


    def display(self):
        print(self.q)

q=Queue(3)
q.enqueue(5)
q.enqueue(54)
q.enqueue(52)
q.enqueue(57)
q.dequeue()
q.dequeue()
q.enqueue(5455)
q.display()



        
