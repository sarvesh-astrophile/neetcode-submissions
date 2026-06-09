from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        # Array to store the min of left_max and right_max for each position
        final = [0] * n
        total_water = 0

        # 1. Compute prefix max (from left to right)
        prefix_max = 0
        for i in range(n):
            prefix_max = max(prefix_max, height[i])
            final[i] = prefix_max   # final[i] temporarily holds left_max[i]

        # 2. Compute postfix max (from right to left) and update final
        postfix_max = 0
        for i in range(n - 1, -1, -1):
            postfix_max = max(postfix_max, height[i])
            # final[i] becomes min(left_max[i], right_max[i])
            final[i] = min(final[i], postfix_max)

        # 3. Calculate trapped water
        for i in range(n):
            total_water += final[i] - height[i]

        return total_water