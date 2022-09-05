class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
class Binarytree:
    def __init__(self):
        self.root=None
        

# if __name__== '__main__':
ob1=Binarytree()
frist=Node(1)
second=Node(2)
third=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)
seven=Node(7)
ob1.root=frist
print(ob1.root.val)
frist.left=second
frist.right=third
second.left=four
second.right=five
third.left=six
third.right=seven
#print(second.left.data)
        