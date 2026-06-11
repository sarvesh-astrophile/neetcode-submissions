class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for idx, num in enumerate(nums):
            if num > 0:
                break

            if idx > 0 and nums[idx - 1] == num:
                continue

            l, r = idx + 1, len(nums) - 1
            while l < r:
                sum_value = num + nums[l] + nums[r]
                if sum_value > 0:
                    r -= 1
                elif sum_value < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1

        return result
