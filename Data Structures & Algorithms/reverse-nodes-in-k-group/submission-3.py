# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # init previous_group_end
        dummy = ListNode(0, head)
        previous_group_end = dummy

        # loop
        while True:
            # find the kth element
            kth = previous_group_end
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # seprate the group
            group_start = previous_group_end.next
            next_group = kth.next

            # reverse the group
            prev = next_group
            curr = group_start
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # reattach to main line
            previous_group_end.next = prev            
            # previous_group_end move
            previous_group_end = group_start