class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printLevelOrder(root):
    if root is None:
        return 
    queue=[]
    queue.append(root)
    while queue:
        print(queue[0].data,end=" ")
        node=queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
root=Node(5)
root.left=Node(6)
root.right=Node(7)
root.left.left=Node(8)
root.left.right=Node(9)
root.right.left=Node(10)
root.right.right=Node(11)
printLevelOrder(root)
        