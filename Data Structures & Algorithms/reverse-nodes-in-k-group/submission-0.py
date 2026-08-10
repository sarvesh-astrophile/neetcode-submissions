# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group_end = dummy

        while True:
            # 1. Check if there are at least k nodes left
            kth = prev_group_end
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # 2. Detach the group
            group_start = prev_group_end.next
            next_group = kth.next

            # 3. Reverse exactly k nodes
            prev = next_group
            curr = group_start
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 4. Reattach: prev is the new head of the reversed group
            prev_group_end.next = prev
            # Move prev_group_end to the new tail (which was group_start)
            prev_group_end = group_start