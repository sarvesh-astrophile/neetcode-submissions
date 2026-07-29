# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1 number
        num1 = 0
        n, curr = 0, l1

        while curr:
            num1 += curr.val * (10 ** n)
            n += 1
            curr = curr.next

        # l2 number
        num2 = 0
        n, curr = 0, l2

        while curr:
            num2 += curr.val * (10 ** n)
            n += 1
            curr = curr.next

        sum_value = num1 + num2

        if sum_value == 0:
            return ListNode(0)

        # add and convert to List Node

        dummyNode = ListNode()
        head = dummyNode
        while sum_value != 0:
            remainder = sum_value % 10
            quotient = sum_value // 10
            dummyNode.next = ListNode(remainder)
            sum_value = quotient
            dummyNode = dummyNode.next

        return head.next