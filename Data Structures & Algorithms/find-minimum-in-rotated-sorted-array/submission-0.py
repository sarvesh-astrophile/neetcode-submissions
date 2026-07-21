class Solution:
    def findMin(self, nums: List[int]) -> int:
        minN = nums[0]
        for num in nums:
            minN = min(minN, num)

        return minN