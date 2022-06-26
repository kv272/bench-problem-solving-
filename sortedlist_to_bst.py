nums=[1,2,3,4,5,6,7,8,9,10]
class TreeNode:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
def solve(arr=nums):
    if len(arr) == 0:
        return None
    i=0
    j=len(arr)-1
    mid = (i+j)//2
    node = TreeNode(arr[mid],None,None)
    node.left = solve(arr[:mid])
    node.right = solve(arr[mid+1:])
    return node
root=solve()
def inorder(root):
    if root==None:
        return 
    print(root.data)
    inorder(root.left)
    inorder(root.right)
inorder(root)