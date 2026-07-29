# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finding the middle
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # mergeing 
        list1, list2 = head, prev
        while list2.next:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2