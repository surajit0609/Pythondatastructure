class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doublylinkedlist:
    def __init__(self):
        self.head=None
    def get_length(self):
        length=0
        temp=self.head
        while temp is not None:
            length+=1
            temp=temp.next
        return length
    def insert_first(self,data):
        B_Node=Node(data)
        if self.head is None:
            self.head=B_Node
        else:
            B_Node.next=self.head
            self.head.prev=B_Node
            self.head=B_Node
    def insert_last(self,data):
        L_Node=Node(data)
        if self.head is None:
            self.head=L_Node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=L_Node
            L_Node=temp.prev
    def insert_pos(self,data,pos):
        PN=Node(data)
        if self.head is None:
            self.head=PN
        else:
            index=0
            temp=self.head
            for index in range(pos-1):
                temp=temp.next
            PN.next=temp.next
            temp.next.prev=PN
            PN.prev=temp
            temp.next=PN
    def delete_first(self):
        if self.head is None:
            print("empty list")
        else:
            self.head=self.head.next
            self.head.next.prev=None
    def delete_last(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            prev1=self.head
            while temp.next is not None:
                prev1=temp
                temp=temp.next
            prev1.next=None
    def delete_pos(self,pos):
        if self.head is None:
            print("empty list")
        else: 
            index=0
            temp=self.head
            for index in range(pos-1):
                temp=temp.next
            temp.next=temp.next.next
            temp.next.prev=temp 
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,"-->",sep="",end="")
            temp=temp.next
        print()
LL=Doublylinkedlist()
LL.insert_first(12)
LL.insert_first(13)
LL.insert_first(14)
LL.insert_first(15)
LL.insert_last(76)
LL.insert_last(77)
LL.insert_last(78)
LL.insert_last(79)
LL.insert_pos(56,2)
print(LL.get_length())
LL.display()
LL.delete_first()
print(LL.get_length())
LL.display()
LL.delete_last()
print(LL.get_length())
LL.display()
LL.delete_pos(2)
print(LL.get_length())
LL.display()


