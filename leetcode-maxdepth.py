class Solution(object):
    max1=0
    def maxDepth(self, root):
        if root==None:
            return 0
        max1=max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)
        return max1
