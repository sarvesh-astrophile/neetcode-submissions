class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # algo floid 
        # find the comman with fast and slow
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # use second slow with fast to find repeat
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            fast = nums[fast]

            if fast == slow2:
                return fast