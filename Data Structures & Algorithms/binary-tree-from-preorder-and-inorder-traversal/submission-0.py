# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i
        idx=0
        def solve(start,end):
            nonlocal idx
            if start>end:
                return None
            val=preorder[idx]
            idx+=1
            node=TreeNode(val)
            node.left=solve(start,d[val]-1)
            node.right=solve(d[val]+1,end)
            return node
        return solve(0,len(preorder)-1)