class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # init
        n = len(heights)
        # find leftmax
        stack = []
        leftmax = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                leftmax[i] = stack[-1]

            stack.append(i)

        # find rightmax
        stack = []
        rightmax = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                rightmax[i] = stack[-1]

            stack.append(i)

        # calcuate the area and compare
        maxArea = 0
        for i in range(n):
            leftmax[i] += 1
            rightmax[i] -= 1
            maxArea = max(maxArea, (rightmax[i] - leftmax[i] + 1) * heights[i])

        return maxArea
