# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        common=[]
        def find(root,subRoot):
            nonlocal common
            if not root:
                return None
            if root.val==subRoot.val:
                common.append(root)
            find(root.left,subRoot)
            find(root.right,subRoot)
            
        def solve(p,q):
            if not q and not p:
                return True
            if not q or not p:
                return False
            if q.val!=p.val:
                return False
            return solve(p.left,q.left) and solve(p.right,q.right)
            
        

        find(root,subRoot)
        for node in common:
            if solve(node,subRoot):
                return True
        return False

        