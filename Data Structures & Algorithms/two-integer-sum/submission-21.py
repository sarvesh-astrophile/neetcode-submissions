class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)

        for i in range(len(nums)):
            num_dict[nums[i]] = i

        for l in range(len(nums)):
            index = target - nums[l]
            if index in num_dict and l != num_dict[index]:
                return [min(l, num_dict[index]), max(l, num_dict[index])]