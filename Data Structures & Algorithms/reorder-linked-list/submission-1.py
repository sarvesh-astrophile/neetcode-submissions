class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the middle of the list (slow/fast pointer)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half (starting from slow)
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # Now 'prev' is the head of the reversed second half

        # 3. Merge the two halves: first half (head to before slow) and reversed second half (prev)
        first, second = head, prev
        while second.next:  # Stop when the last node of second half is reached
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2