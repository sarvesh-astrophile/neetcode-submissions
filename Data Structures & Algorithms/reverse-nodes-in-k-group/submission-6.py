class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # init, previous_group
        previous_group = dummy = ListNode(0, head)

        while True:
            # kth element
            kth = previous_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # init group elements, disconnect
            group_start = previous_group.next
            next_group = kth.next

            # reverse
            prev = next_group
            curr = group_start
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # connect back to main
            previous_group.next = prev
            previous_group = group_start