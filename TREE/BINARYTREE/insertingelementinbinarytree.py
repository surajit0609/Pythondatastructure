### insertelement in binary tree
class Binarrytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insertleft(self,newnode):
        if self.left == None:
            self.left=Binarrytree(newnode)
        else:
            temp=Binarrytree(newnode)
            temp.left=self.left
            self.left=temp
    def insertright(self,newNode):
        if self.right==None:
            self.right=Binarrytree(newNode)
        else:
            temp=Binarrytree(newNode)
            temp.right=self.right
            self.right=temp
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def inOrder(root):
    if root :
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)

root=Binarrytree(10)
root.left=Binarrytree(8)
root.right=Binarrytree(2)
root.left.left=Binarrytree(3)
root.left.right=Binarrytree(5)
root.right.left=Binarrytree(2)
preorder(root)
root.insertleft(56)
##print("uyas",root.left.data)
preorder(root)
