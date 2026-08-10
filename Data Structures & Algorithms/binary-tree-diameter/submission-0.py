# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=0
        def solve(root):
            nonlocal dia
            if not root:
                return 0
            left=1+solve(root.left)
            right=1+solve(root.right)
            dia=max(dia,left+right-2)
            return max(left,right)
        solve(root)
        return dia