class Stack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.stack=[]
    def push(self,data):
        if len(self.stack)==self.capacity:
            print("overflow")
        else:
            self.stack.append(data)
    def isempty(self):
        return len(self.stack)==0
    def pop(self):
        if len(self.stack)==0:
            print("empty stack")
        else:
            v=self.stack.pop(-1)
            print(v)
    def peek(self):
        if (self.isempty()):
            print("empty")
        else:
            s=self.stack(-1)
            print(s)
         
    def display(self):
        return self.stack   
s=Stack(2)
print(s.isempty())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.pop()
print(s.isempty())
print(s.display())
        