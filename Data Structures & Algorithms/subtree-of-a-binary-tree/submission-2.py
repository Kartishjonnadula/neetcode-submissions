# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isit(root,node):
            if not root and not node:
                return True
            if not root or not node or root.val!=node.val:
                return False
            return isit(root.left,node.left) and isit(root.right,node.right)
        def solve(root):
            if not root:
                return False
            if root.val==subRoot.val:
                if isit(root,subRoot):
                    return True
            return  solve(root.right) or solve(root.left)
        return solve(root)