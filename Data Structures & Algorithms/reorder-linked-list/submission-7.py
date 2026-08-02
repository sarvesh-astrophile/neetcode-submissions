# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # init
        # find the middle
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd part
        prev = None
        curr = slow
        while curr:
            temp1 = curr.next
            curr.next = prev
            prev = curr
            curr = temp1

        # merge both parts
        first, second = head, prev
        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
