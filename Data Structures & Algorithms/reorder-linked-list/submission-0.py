# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def mid(head):
            slow,fast=head,head
            prev=None
            while fast and fast.next:
                prev=slow
                fast=fast.next.next
                slow=slow.next
            return slow
        def reverse(head):
            curr=head
            next=curr.next
            prev=None
            #  1 2 3 4
            while curr:
                # temp=next.next
                curr.next=prev
                prev=curr
                curr=next
                if next:
                    next=next.next
            return prev
        middle=mid(head)
        second=reverse(middle)
        first=head
        res=ListNode()
        temp=res
        i=0
        print(first.val)
        # print()
        # 5 6 7 8.  6
        # 1 - 5 -2 -3-7-4-8
        while second.next:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2
        
            