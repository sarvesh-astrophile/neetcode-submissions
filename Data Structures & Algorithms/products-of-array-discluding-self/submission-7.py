class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix_product = 1
        for i in range(len(nums)):
            result[i] *= prefix_product
            prefix_product *= nums[i]

        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result
