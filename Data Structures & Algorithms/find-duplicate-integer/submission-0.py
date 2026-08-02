class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floyed algo
        slow = fast = 0
        # find the intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

       # reach the start of cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
