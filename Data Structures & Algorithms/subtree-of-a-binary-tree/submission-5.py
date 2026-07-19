# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and not root :
            return True
        if not root:
            return False
        if self.check(root,subRoot):
            return True
        else:
            return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
    def check(self,tree,sub): # lets perform dfs check
        if not tree and not sub:
            return True
        if tree and sub and  tree.val==sub.val:
            left=self.check(tree.left,sub.left)
            right=self.check(tree.right,sub.right)
            return left and right
        else:
            return False

        