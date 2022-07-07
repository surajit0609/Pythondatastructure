class StackNode:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.root=None
    def isempty(self):
        if self.root is None:
            return True
        else:
            return False
    def push(self,data):
        newstacknode=StackNode(data)
        newstacknode.next=self.root
        self.root=newstacknode
        print ("% d pushed to stack" % (data))
    def pop(self):
        if (self.isempty()):
            return
        temp=self.root
        self.root=self.root.next
        popped=temp.data
        return popped
    def peek(self):
        return self.root.data
s2=Stack()
s2.push(45)
s2.push(67)
s2.push(48)
s2.push(69)
s2.push(40)
s2.push(62)
print ("% d popped from stack" % (s2.pop()))
print ("Top element is % d " % (s2.peek()))
                