class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use fast and slow to find intersection
        fast = slow = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # then use another slow to find the start
        slow2 = nums[0]
        while True:
            if slow2 == slow:
                return slow

            slow = nums[slow]
            slow2 = nums[slow2]