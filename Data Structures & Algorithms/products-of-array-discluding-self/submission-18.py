class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, postfix = [1] * n, [1] * n

        for i in range(n):
            if i > 0:
                prefix[i] = prefix[i - 1] * nums[i - 1]
                j = n - i - 1
                postfix[j] = postfix[j + 1] * nums[j + 1]

        result = [1] * n
        for i in range(n):
            result[i] = prefix[i] * postfix[i]

        return result
