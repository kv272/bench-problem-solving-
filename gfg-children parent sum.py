
class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        left=0
        right=0
        if root==None or(root.left==None and root.right==None):
            return 1
        else:
            if root.left!=None:
                left=root.left.data
            if root.right!=None:
                right=root.right.data
            if left+right==root.data and self.isSumProperty(root.left) and self.isSumProperty(root.right):
                return 1
            else:
                return 0
