# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node,prev):
            if not node:
                return 0
            if node.val >= prev:
                left= helper(node.left,node.val)
                right= helper(node.right,node.val)
                return 1+left+right
            elif node.val < prev:
                left= 0+helper(node.left,prev)
                right= 0+helper(node.right,prev)
                return left+right

        return helper(root,float('-inf'))
            
        