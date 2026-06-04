class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSorted = []
        for i, num in enumerate(nums):
            numsSorted.append([num, i])
        
        numsSorted.sort()

        i, j = 0, len(numsSorted) - 1
        while j > i:
            sortedSum = numsSorted[i][0] + numsSorted[j][0]
            if sortedSum == target:
                return [min(numsSorted[i][1], numsSorted[j][1]), max(numsSorted[i][1], numsSorted[j][1])]
            elif sortedSum > target:
                j -= 1
            elif sortedSum < target:
                i += 1

        return []

        