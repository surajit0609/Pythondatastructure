class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
def preorder(root):
    if root:
        print(root)
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

    
root=Node(10)
root.left=Node(8)
root.right=Node(2)
root.left.left=Node(3)
root.left.right=Node(5)
root.right.left=Node(2)
#print ("Preorder traversal of binary tree is")
#preorder(root)
print ("\nInorder traversal of binary tree is")
inOrder(root)
#print ("\nPostorder traversal of binary tree is")
#postOrder(root)