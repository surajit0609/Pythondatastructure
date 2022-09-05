class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def inOrder(root):
    current=root
    stack=[]
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        elif(stack):
            current=stack.pop()
            print(current.val,end=" ")
            current=current.right
        else:
            break
    print()





root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
if __name__ == "__main__":
    inOrder(root)
