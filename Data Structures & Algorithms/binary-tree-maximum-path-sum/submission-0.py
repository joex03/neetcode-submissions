# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            left=helper(node.left)
            right=helper(node.right)
            leftMax=max(left,0)
            rightMax=max(right,0)
            self.res=max(self.res,node.val+leftMax+rightMax)
            return node.val+max(leftMax,rightMax)
        helper(root)
        return self.res
        