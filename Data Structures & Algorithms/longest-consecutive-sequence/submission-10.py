class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for idx, num in enumerate(nums):
            if num - 1 in nums_set:
                continue

            length = 0
            while num + length in nums_set:
                length += 1
                longest = max(longest, length)
        
        return longest
                