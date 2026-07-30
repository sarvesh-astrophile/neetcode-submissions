# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. dummy node
        dummyNode = ListNode(0, head)

        # 2. create fast node with space
        slow = dummyNode
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1

        # 3. reach the n - 1 th node
        while fast:
            slow = slow.next
            fast = fast.next

        # 4. remove the nth node
        slow.next = slow.next.next

        return dummyNode.next