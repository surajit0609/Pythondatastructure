class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
    def hight(root):
        if root is None:
            return 0
        else:
            lhight=(root.left)
            rhight=(root.right)
            return max(lhight,rhight) +1

        