class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # flyod algorithm
        # init
        # find the meet of fast and slow
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # find the start of cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow