# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[(node.val,i,node) for i,node in enumerate(lists) if node]
        head=ListNode()
        heapq.heapify(heap)
        prev=head
        c=len(lists)
        while heap:
            _,_,node=heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap,(node.next.val,c,node.next))
                c+=1
            prev.next=node
            prev=node
        return head.next
            
            