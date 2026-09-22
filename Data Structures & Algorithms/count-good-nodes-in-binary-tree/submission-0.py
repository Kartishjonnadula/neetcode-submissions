# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from math import inf
        ans=0
        def solve(root,m):
            nonlocal ans
            if not root:
                return 
            if root.val>=m:
                ans+=1
            solve(root.left,max(m,root.val))
            solve(root.right,max(m,root.val))
        solve(root,-inf)
        return ans
        