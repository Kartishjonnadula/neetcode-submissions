# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def find(root):
            if not root:
                return None
            if root.val==subRoot.val:
                if check(root,subRoot):
                    return root
            node=find(root.left)
            if node:
                return node
            node=find(root.right)
            if node:
                return node
            return None
        def check(root1,root2):
            if not root1 and not root2:
                return True
            if not root1:
                return False
            if not root2:
                return False

            if root1.val!=root2.val:
                return False
            if check(root1.left,root2.left) and check(root1.right,root2.right):
                return True
            return False
        root=find(root)
        print(root)
        if root:
            return True
        return False