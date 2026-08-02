class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        def get_kth_node(start: ListNode, k: int):
            while start and k >1:
                start = start.next
                k -= 1
            return start
        def reverse(node):
            prev=None
            curr=node
            nnode=curr.next
            while curr:
                nnode=curr.next
                curr.next=prev
                prev=curr
                curr=nnode
            return prev
        previous_group=None
        start=head
        while True:
            kth_node=get_kth_node(start,k)
            if not kth_node:
                break

            next_node=kth_node.next
            kth_node.next=None
            reverse_head=reverse(start)
            if start==head:
                head=reverse_head #or kth node
            else:
                previous_group.next=reverse_head
            start.next=next_node
            previous_group=start
            start=next_node
        return head
                
                