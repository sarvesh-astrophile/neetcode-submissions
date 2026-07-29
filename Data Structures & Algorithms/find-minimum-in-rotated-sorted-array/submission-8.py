class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        minN = nums[r]
        while l <= r:
            mid = l + (r - l) // 2

            if nums[l] <= nums[r]:
                minN = min(minN, nums[l])

            minN = min(minN, nums[mid])
            
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return minN