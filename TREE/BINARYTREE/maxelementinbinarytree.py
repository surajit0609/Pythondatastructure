class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
maxdata=float("-inf")
def maxelsment(root):
    global maxdata
    if root is None:
        return maxdata
    if root.data > maxdata:
        maxdata = root.data
    maxelsment(root.left)
    maxelsment(root.right)
    return maxdata


root=Node(10)
root.left=Node(8)
root.right=Node(2)
root.left.left=Node(3)
root.left.right=Node(5)
root.right.left=Node(2)
v=maxelsment(root)
print(v)