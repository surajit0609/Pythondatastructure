class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def postorder(root):
    if root is None:
        return
    s1=[]
    s2=[]
    s1.append(root)
    while (len(s1)>0):
        node=s1.pop()
        s2.append(node)
        if node.left is not None:
            s1.append(node.left)
        if node.right is not None:
            s1.append(node.right)
    while (len(s2)>0):
        node=s2.pop()
        print(node.data,end=" ")
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
postorder(root)
        