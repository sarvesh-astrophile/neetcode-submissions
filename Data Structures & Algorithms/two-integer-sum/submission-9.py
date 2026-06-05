class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = defaultdict(int)
        for idx, num in enumerate(nums):
            num_set[num] = idx

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in num_set and i != num_set[diff]:
                return [min(i, num_set[diff]), max(i, num_set[diff])]

        return []