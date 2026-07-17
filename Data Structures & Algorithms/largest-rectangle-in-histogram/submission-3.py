class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        # left[i] will be the first index of the widest rectangle using height[i]
        left = [0] * n
        for i in range(n):
            # Pop bars that are taller or equal, they can't be the left boundary
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # If stack is empty, no smaller bar on the left → start at 0
            # Else, start right after the nearest smaller bar on the left
            left[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)

        stack = []
        # right[i] will be the last index of the widest rectangle using height[i]
        right = [n - 1] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # If stack is empty, no smaller bar on the right → end at n-1
            # Else, end right before the nearest smaller bar on the right
            right[i] = n - 1 if not stack else stack[-1] - 1
            stack.append(i)

        maxArea = 0
        for i in range(n):
            width = right[i] - left[i] + 1
            maxArea = max(maxArea, heights[i] * width)

        return maxArea