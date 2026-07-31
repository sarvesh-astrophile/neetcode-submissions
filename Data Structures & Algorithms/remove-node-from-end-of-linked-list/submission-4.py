# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init
        first = dummy = ListNode(0, head)
        second = head

        # 1. make two pointers
        while n > 0:
            second = second.next
            n -= 1

        # 2. find the Node and delete it
        while second:
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next