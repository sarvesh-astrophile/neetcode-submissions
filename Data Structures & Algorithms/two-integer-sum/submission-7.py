class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = []
        for idx, num in enumerate(nums):
            sorted_nums.append([num, idx])

        sorted_nums = sorted(sorted_nums, key=lambda item: item[0], reverse=False)

        i, j = 0, len(nums) - 1
        for idx in range(len(nums) - 1):
            curr_sum = sorted_nums[i][0] + sorted_nums[j][0]

            if curr_sum == target:
                return [min(sorted_nums[i][1], sorted_nums[j][1]),
                    max(sorted_nums[i][1], sorted_nums[j][1])]
            elif curr_sum < target:
                i += 1
            elif curr_sum > target:
                j -= 1

        return []