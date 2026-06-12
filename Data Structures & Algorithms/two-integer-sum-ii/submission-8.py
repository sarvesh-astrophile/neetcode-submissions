class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_dict = defaultdict(int)

        for idx, num in enumerate(numbers):
            nums_dict[num] = idx

        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in nums_dict:
                return [idx + 1, nums_dict[diff] + 1]

        return []