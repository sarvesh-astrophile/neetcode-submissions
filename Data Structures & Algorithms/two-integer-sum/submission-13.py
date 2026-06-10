class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = defaultdict(int)

        for idx, num in enumerate(nums):
            num_index[num] = idx

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_index and num_index[diff] != idx:
                return [idx, num_index[diff]]

        return []