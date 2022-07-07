class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
class circular_LL:
    def __init__(self):
        self.head=None
    def insert_first(self,data):
        nf=Node(data)
        if self.head  is None:
            self.head=nf
            nf.next=self.head 
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=nf
            nf.next=self.head
            self.head=nf   
    def insert_last(self,data):
        nl=Node(data)
        if self.head  is None:
            self.head=nl
            nl.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=nl
            nl.next=self.head
    def display(self):
        temp=self.head
        while temp is not self.head:
            print(temp.data,"-->",end="")
            temp=temp.next
        print(temp.data)

l=circular_LL()
l.insert_first(67)
l.insert_first(76)
l.display()
            