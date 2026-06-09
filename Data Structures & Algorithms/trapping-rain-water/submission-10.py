class Solution:
    def trap(self, height: List[int]) -> int:
        final = [0] * len(height)
        result = 0

        if len(height) == 0:
            return 0

        # prefix
        prefix_max = 0
        for i in range(len(height) - 1):
            prefix_max = max(height[i], prefix_max)
            final[i] = prefix_max

        # postfix
        postfix_max = 0
        for i in range(len(height) - 1, -1, -1):
            postfix_max = max(height[i], postfix_max)
            final[i] = min(postfix_max, final[i])

        # remove current height
        for i in range(len(height) - 1):
            result += max(0, final[i] - height[i])

        return result