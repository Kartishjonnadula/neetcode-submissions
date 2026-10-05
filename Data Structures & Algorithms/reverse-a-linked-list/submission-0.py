# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def solve(head):
            if not head:
                return head
            curr=head
            next=head.next
            prev=None
            while next:
                curr.next=prev
                prev=curr
                curr=next
                next=next.next
            curr.next=prev
            return curr
        return solve(head)