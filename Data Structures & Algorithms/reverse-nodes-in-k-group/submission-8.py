# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_group = dummy = ListNode(0, head)

        while prev_group:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_start = prev_group.next
            group_end = kth.next

            prev = group_end
            curr = group_start
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            prev_group.next = prev
            prev_group = group_start 