# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m=n
        temp1=head
        while temp1 and n>0:
            n-=1
            temp1=temp1.next
        res=head
        prev=None
        while temp1:
            temp1=temp1.next
            prev=res
            res=res.next
        if prev:
            prev.next=res.next
        else:
            head=head.next
        return head
        