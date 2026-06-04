class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_array = []
        i, j = 0, len(nums) - 1
        for idx, num in enumerate(nums):
            sorted_array.append([num, idx])

        sorted_array = sorted(sorted_array, key=lambda x: x[0])

        while i < j:
            two_sum = sorted_array[i][0] + sorted_array[j][0]
            if  two_sum == target:
                return [min(sorted_array[i][1], sorted_array[j][1]), 
                max(sorted_array[i][1], sorted_array[j][1])]
            elif two_sum > target:
                j -= 1
            elif two_sum < target:
                i += 1
            
        return []
