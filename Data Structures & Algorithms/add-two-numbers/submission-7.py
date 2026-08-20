# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # init dummy
        curr = dummy = ListNode()

        # item1, item2 and carry to add
        carry = 0
        while l1 or l2 or carry:
            item1 = l1.val if l1 else 0
            item2 = l2.val if l2 else 0

            sum_val = item1 + item2 + carry
            new_val = sum_val % 10
            carry = int(sum_val / 10)

            # create node and connect to prev
            curr.next = ListNode(val=new_val)

            # move all nodes
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # return dummy next
        return dummy.next