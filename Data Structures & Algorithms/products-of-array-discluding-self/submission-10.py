class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # prefix
        prefix = [1] * (len(nums) + 1)
        for i in range(len(nums) -1):
            prefix[i + 1] = prefix[i] * nums[i]

        # postfix
        postfix = [1] * (len(nums) + 1)
        for i in range(len(nums) -1, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i + 1]

        return result