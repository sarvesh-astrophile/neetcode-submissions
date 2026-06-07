class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            count = 1
            if (num - 1) in num_set:
                continue
            
            while (num + count) in num_set:
                count += 1

            if count > longest:
                longest = count

            
        return longest

        