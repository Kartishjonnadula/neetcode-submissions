# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s=""
        def solve(root):
            nonlocal s
            if not root:
                s+=("*#")
                return
            s+=str(root.val)+'#'
            solve(root.left)
            solve(root.right)
        solve(root)
        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data=data.split("#")
        print(data)
        i=0
        def solve():
            nonlocal i
            # if i==len(data):
            #     return None
            if data[i]=='*':
                i+=1
                return None
            node=TreeNode(data[i])
            i+=1
            node.left=solve()
            node.right=solve()
            return node

        node=solve()

        return node