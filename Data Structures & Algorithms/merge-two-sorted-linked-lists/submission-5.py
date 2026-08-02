# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # init, dummy
        head = dummy = ListNode()

        # compare and add to dummy
        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next

            dummy = dummy.next

        # put the rest at the end if there
        if list1:
            dummy.next = list1
        
        if list2:
            dummy.next = list2

        return head.next