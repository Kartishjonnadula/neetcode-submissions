"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d={}
        curr=head
        prev=None
        while curr:
            if curr not in d:
                d[curr]=Node(curr.val)
            node=d[curr]
            node.next=curr.next
            if curr.random not in d:
                d[curr.random]=Node(curr.random.val) if curr.random else None
            node.random=d[curr.random]
            if prev:
                prev.next=node
            prev=node
            curr=curr.next
        return d[head]            
            