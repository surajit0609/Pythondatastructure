
class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
def preorder(root):
    if root is None:
        return
    nodestack=[]
    nodestack.append(root)
    while(len(nodestack)>0):
        node=nodestack.pop()
        print(node.data,end=" ")
        if node.right is not None:
            nodestack.append(node.right)
        if node.left is not None:
            nodestack.append(node.left)
root=Node(10)
root.left=Node(8)
root.right=Node(2)
root.left.left=Node(3)
root.left.right=Node(5)
root.right.left=Node(2)
preorder(root)