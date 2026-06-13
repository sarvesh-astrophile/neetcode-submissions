class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for idx, a in enumerate(nums):
            if a > 0:
                break

            if nums[idx - 1] == a and idx > 0:
                continue

            l, r = idx + 1, len(nums) - 1
            while l < r:
                sum_value = a + nums[l] + nums[r]
                if sum_value > 0:
                    r -= 1
                elif sum_value < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result