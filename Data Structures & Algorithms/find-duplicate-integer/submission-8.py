class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyed algo
        # init fast and slow
        fast = slow = nums[0]

        # find the meet point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # use slow2 to find the repeat
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow