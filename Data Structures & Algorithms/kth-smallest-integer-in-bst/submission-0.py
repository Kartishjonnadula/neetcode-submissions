# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=False
        index=0
        def solve(root):
            nonlocal index,ans
            if ans:
                return
            if not root:
                return
            solve(root.left)
            index+=1
            if index==k:
                ans=root.val
            solve(root.right)
        solve(root)
        return ans
        