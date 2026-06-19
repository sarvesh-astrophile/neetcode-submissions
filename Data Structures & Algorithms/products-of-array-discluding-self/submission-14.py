class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] * nums[i]

        postfix = [1] * (len(nums) + 1)
        for i in range(len(nums) -1, -1, -1):
            postfix[i - 1] = postfix[i] * nums[i]

        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]

        return result
        