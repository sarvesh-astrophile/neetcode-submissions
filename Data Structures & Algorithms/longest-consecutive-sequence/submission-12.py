class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxS = 0

        for i in range(len(nums)):
            if nums[i] -1 in nums_set:
                continue

            count = 1
            while (nums[i] + count) in nums_set:
                count += 1

            maxS = max(maxS, count)

        return maxS