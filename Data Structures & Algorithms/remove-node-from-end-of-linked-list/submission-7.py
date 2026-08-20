# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init
        left = dummy = ListNode(0, head)
        right = head

        # move right with n moves
        for _ in range(n):
            right = right.next

        # move left and right both untill it reach end
        while right:
            right = right.next
            left = left.next

        # remove the node
        left.next = left.next.next

        return dummy.next
