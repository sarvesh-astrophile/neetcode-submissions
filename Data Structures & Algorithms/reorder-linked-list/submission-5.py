# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse the 2nd part
        prev = None
        curr = slow

        while curr:
            temp1 = curr.next
            curr.next = prev
            prev = curr
            curr = temp1

        # 3. merge the 1st and 2nd part
        l1, l2 = head, prev
        while l2.next:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2
