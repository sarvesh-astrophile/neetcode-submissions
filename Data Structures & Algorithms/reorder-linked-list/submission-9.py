class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split in half and find middle
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # join them
        sec = prev
        fir = head
        while fir and sec:
            temp1 = fir.next
            temp2 = sec.next

            fir.next = sec
            sec.next = temp1

            fir = temp1
            sec = temp2