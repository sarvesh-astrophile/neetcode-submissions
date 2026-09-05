# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer to get to prev of Nth node
        right = dummy = ListNode(0, head)
        left = dummy
        for _ in range(n):
            right = right.next

        # get to node to remove
        while right.next:
            left = left.next
            right = right.next

        # remove the node
        left.next = left.next.next

        return dummy.next