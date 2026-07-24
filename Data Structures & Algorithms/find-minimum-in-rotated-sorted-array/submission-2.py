class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        minNum = nums[0]
        while l <= r:
            m = l + (r - l) // 2

            if l <= r:
                minNum = min(minNum, nums[l])

            minNum = min(minNum, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return minNum