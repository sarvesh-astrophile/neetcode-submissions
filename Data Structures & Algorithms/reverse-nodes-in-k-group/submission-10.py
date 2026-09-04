# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # init, prev_group
        prev_group = dummy = ListNode(0, head)

        while True:
            # kth move
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # disconnect
            group_start = prev_group.next
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
            prev_group.next = prev
            prev_group = group_start