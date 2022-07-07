class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlylinkedlist:
    def __init__(self):
        self.head=None
    def length(self):
        leng=0
        temp=self.head
        while temp is not None:
            leng+=1
            temp=temp.next
        return leng
    def insert_first(self,data):
        BN=Node(data)
        if self.head is None:
            self.head=BN
        else:
            BN.next=self.head
            self.head=BN
    def insert_end(self,data):
        EN=Node(data)
        if self.head is None:
            self.head=EN
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=EN
    def insert_pos(self,data,pos):
        PN=Node(data)
        if self.head is None:
            self.head=PN
        index=0
        temp=self.head
        for index in range(pos-1):
            temp=temp.next
        PN.next=temp.next
        temp.next=PN
    def delet_first(self):
        if self.head is None:
            print("empty linked list")
        else:
            self.head=self.head.next
    def delet_end(self):
        if self.head is None:
            print("empty linked list")
        else:
            priv=self.head
            current=self.head
            while current.next is not None:
                priv=current
                current=current.next
            priv.next=None
    def delet_pos(self,pos):
        index=0
        temp=self.head
        for index in range(pos-1):
            temp=temp.next
        temp.next=temp.next.next
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,"-->",sep="",end='')
            temp=temp.next
        print()
LL=Singlylinkedlist()
LL.insert_first(65)
LL.insert_first(66)
LL.insert_first(67)
LL.insert_first(68)
LL.insert_end(69)
LL.insert_end(45)
LL.insert_end(76)
LL.insert_end(23)
LL.insert_pos(60,3)
LL.insert_pos(70,4)
LL.insert_pos(91,5)
LL.insert_pos(92,6)
print(LL.length())
LL.display()
LL.delet_first()
print(LL.length())
LL.display()
LL.delet_end()
print(LL.length())
LL.display()
LL.delet_pos(2)
print(LL.length())
LL.display()
        

            