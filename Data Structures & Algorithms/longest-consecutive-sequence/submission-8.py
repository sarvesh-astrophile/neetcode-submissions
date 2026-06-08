class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for idx, num in enumerate(nums):
            length = 1

            if (num - 1) in num_set:
                continue

            while (num + length) in num_set:
                length += 1

            longest = max(length, longest)

        return longest

            
            

        