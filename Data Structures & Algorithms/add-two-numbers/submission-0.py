# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        temp=res
        borrow=0
        while l1 or l2:
            curr_sum=(l1.val if l1 else 0 )+(l2.val if l2 else 0)+borrow
            borrow=curr_sum//10
            curr=curr_sum%10
            node=ListNode(curr)
            temp.next=node
            temp=node
            l1,l2=(l1.next if l1 else None),(l2.next if l2 else None)
        if borrow!=0:
            node=ListNode(borrow)
            temp.next=node
            temp=node
        return res.next