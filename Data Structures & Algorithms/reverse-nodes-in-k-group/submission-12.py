# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_group = dummy = ListNode(0, head)

        while True:
            Kth = prev_group
            for _ in range(k):
                Kth = Kth.next
                if not Kth:
                    return dummy.next

            next_group = Kth.next
            group_start = prev_group.next

            prev = next_group
            curr = group_start
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            prev_group.next = prev
            prev_group = group_start