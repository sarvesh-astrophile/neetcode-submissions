# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init
        slow = dummy = ListNode(0, head)

        # moving k time
        fast = head
        for _ in range(n):
            fast = fast.next

        # moving the fast and slow
        while fast:
            fast = fast.next
            slow = slow.next

        # removing and return
        slow.next = slow.next.next

        return dummy.next