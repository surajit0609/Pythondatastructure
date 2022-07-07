class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def getlength(self):
        length=0
        temp=self.head
        while temp is not None:
            length=length+1
            temp=temp.next
        return length       
    def insert_first(self,data):
        firstnode=Node(data)
        if self.head is None:
            self.head=firstnode
            return
        firstnode.next=self.head
        self.head.prev=firstnode
        self.head=firstnode
    def insert_last(self,data):
        lastnode=Node(data)
        if self.head is None:
            self.head=lastnode
            return
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=lastnode
            lastnode.prev=temp
    def insert_middle(self,data,pos):
        nm=Node(data)
        if self.head is None:
            self.head=nm
            return
        else:
            temp=self.head
            i=0
            for i in range(pos-1):
                temp=temp.next
            nm.next=temp.next
            nm.prev=temp
            temp.next=nm
    def delet_first(self):
        if self.head is None:
            print('empty list')
        else:
           self.head=self.head.next
    def delet_last(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end='->')
            temp=temp.next
        print()
l=DoublyLinkedList()
l.insert_first(56)
l.insert_first(67)
l.insert_first(90)
l.insert_last(560)
l.insert_middle(34,2)
print(l.getlength())
l.display()
l.delet_first()
print(l.getlength())
l.display()
l.delet_last()
print(l.getlength())
l.display()
        
        




        

        