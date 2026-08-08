class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd algo
        # find the meet of fast and slow
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # use another slow to find the start of loop
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow