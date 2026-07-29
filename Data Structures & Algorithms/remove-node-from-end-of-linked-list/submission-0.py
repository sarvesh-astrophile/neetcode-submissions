class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse the list
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Remove the n-th node from the beginning (1-indexed)
        if n == 1:
            # Remove the first node of the reversed list
            prev = prev.next
        else:
            curr = prev
            # Move to the (n-1)-th node (the predecessor of the target)
            for _ in range(n - 2):
                curr = curr.next
            # Unlink the target node
            if curr.next:
                curr.next = curr.next.next
        
        # Reverse the list back to original order
        curr = prev
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev