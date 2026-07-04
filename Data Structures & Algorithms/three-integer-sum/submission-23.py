class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) -1
            while l < r:
                sum_value = nums[i] + nums[l] + nums[r]
                if sum_value > 0:
                    r -= 1
                elif sum_value < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result