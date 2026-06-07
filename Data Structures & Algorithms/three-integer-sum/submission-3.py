class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                nums_sum = a + nums[j] + nums[k]
                if nums_sum < 0:
                    j += 1
                elif nums_sum > 0:
                    k -= 1
                else:
                    result.append([a , nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return result