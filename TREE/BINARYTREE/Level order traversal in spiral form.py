###Level order traversal in spiral form with out recoursion
class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def printSpiral(root):
        if root is None:
            return 0
        s1=[]
        s2=[]
        s1.append(root)
        while len(s1) is not None or len(s2) is not None:
            while len(s1) is not None:
                temp = s1[-1]
                s1.pop()
                print(temp.data,end=" ")
                if temp.right is not None:
                    s2.append(temp.right)
                if temp.left is not None:
                    s2.append(temp.left)
            while len(s2) is not None:
                temp=s2[-1]
                s2.pop()
                print(temp.data,end=" ")
                if temp.left is not None:
                    s1.append(temp.left)
                if temp.right is not None:
                    s2.append(temp.right)
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(6)
    root.right.left = newNode(5)
    root.right.right = newNode(4)
    print("Spiral Order traversal of",
                    "binary tree is ")
    printSpiral(root)
        