"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque,defaultdict
        q=deque()
        visited=defaultdict()
        def bfs(root):
            # root=node(node.val)
            # visited[node]=root
            q.append(root)
            copy=Node(root.val)
            visited[root]=copy
            while q:
                node=q.pop()
                # copy=Node(node.val)
                # visited[node]=copy
                for nei in node.neighbors:
                    if nei not in visited:
                        visited[nei]=Node(nei.val)
                        q.append(nei)
                    visited[node].neighbors.append(visited[nei])

            return visited[root]
        if not node:
            return None
        res=bfs(node)
        return res
            