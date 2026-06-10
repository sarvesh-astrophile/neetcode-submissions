class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i - 1] == nums[i] and i > 0:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum_value = nums[i] + nums[l] + nums[r]
                if sum_value > 0:
                    r -= 1
                elif sum_value < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1

        return result


