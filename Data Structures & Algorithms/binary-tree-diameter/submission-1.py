# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l=self.height(root.left)
        r=self.height(root.right)
        diameter=l+r
        return max(diameter,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
    def height(self,node):
        if not node:
            return 0
        left=1+self.height(node.left)
        right=1+self.height(node.right)
        return max(left,right)
        