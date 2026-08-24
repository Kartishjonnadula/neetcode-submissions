# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def solve(root):
            if not root:
                return None
            if root==p or root==q:
                return root
            left=solve(root.left)
            right=solve(root.right)
            if right and left:
                return root
            elif right:
                return right
            else:
                return left
        return solve(root)
        