class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            sum_num = numbers[i] + numbers[j] 
            if sum_num == target:
                return [min(i, j) + 1, max(i, j) + 1]
            elif sum_num < target:
                i += 1
            elif sum_num > target:
                j -= 1
        