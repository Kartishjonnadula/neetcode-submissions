# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(root):
            if not root:
                return None
            
            temp1=solve(root.right)
            temp2=solve(root.left)
            root.left=temp1
            root.right=temp2
            return root
        return solve(root)