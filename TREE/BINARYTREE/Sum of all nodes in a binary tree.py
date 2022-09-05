## whithout recoursio
class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def sumBT(root):
        if root is None:
            return 0
        sum=0
        q=[]
        q.append(root)
        while len(q)>0:
            temp=q.pop(0)
            sum=sum+temp.data
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
        print(sum)
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.right.left.right = newNode(8)
sumBT(root)

 
