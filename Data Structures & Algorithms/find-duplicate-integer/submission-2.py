class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # init flyod algo
        # find the meet of fast and slow in cycle
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # find the entry of cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow