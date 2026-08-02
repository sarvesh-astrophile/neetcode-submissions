# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init, dummy node
        dummy = ListNode(0, head)

        # make two pointer with distance nth
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1

        # delete the node with the previous node with dummy
        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next