class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for idx, num in enumerate(nums):
            indices[num] = idx

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in indices and idx != indices[diff]:
                return [idx, indices[diff]]
            
        return []
        