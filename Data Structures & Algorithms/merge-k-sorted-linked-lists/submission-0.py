# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use 2 list and merge untill all are finished
        while len(lists) > 1:
            head = dummy = ListNode()
            list1, list2 = lists[-1], lists[-2]

            while list1 and list2:
                if list1.val < list2.val:
                    dummy.next = list1
                    list1 = list1.next
                else:
                    dummy.next = list2
                    list2 = list2.next

                dummy = dummy.next

            if list1:
                dummy.next = list1

            if list2:
                dummy.next = list2

            lists.pop()
            lists[-1] = head.next

        return lists[0] if len(lists) != 0 else None