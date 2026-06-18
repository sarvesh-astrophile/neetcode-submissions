class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = defaultdict(int)

        for idx, num in enumerate(nums):
            nums_dict[num] = idx

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict and idx != nums_dict[diff]:
                return [idx, nums_dict[diff]]

        return []