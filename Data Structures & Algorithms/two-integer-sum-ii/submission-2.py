class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set = defaultdict(int)

        for idx, num in enumerate(numbers):
            num_set[num] = idx 

        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in num_set and idx != num_set[diff]:
                return [min(idx, num_set[diff]) + 1, max(idx, num_set[diff]) + 1]

        return []