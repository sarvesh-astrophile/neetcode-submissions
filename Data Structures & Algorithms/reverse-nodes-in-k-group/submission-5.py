# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # init prev_group_end
        prev_group_end = dummy = ListNode(0, head)

        # loop
        while True:
            # moving k times
            kth = prev_group_end
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # disconnect from main
            group_start = prev_group_end.next
            next_group = kth.next

            # reverse
            prev = next_group
            curr = group_start
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # connect to main
            prev_group_end.next = prev
            prev_group_end = group_start