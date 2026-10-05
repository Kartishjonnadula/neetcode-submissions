# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        from math import inf
        ans=-inf
        def solve(root):
            nonlocal ans
            if not root:
                return 0
            y=solve(root.left)
            x=solve(root.right)
            ans=max(ans,root.val+x+y)
            # print(x,y,root.val)
            return max(root.val+max(x,y),0)
        solve(root)
        return ans
        