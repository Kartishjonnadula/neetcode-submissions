# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root,mini,maxi):
            if not root:
                return True
            if root.val>=maxi or root.val<=mini:
                return False
            return solve(root.right,root.val,maxi) and solve(root.left,mini,root.val)
        return solve(root,-inf,inf)
        