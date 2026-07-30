class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 1. init
        n = len(heights)
        maxArea = 0
        # 2. left nearest
        leftMost = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        # 3. right nearest
        rightMost = [n] * n
        stack = []
        for i in range(n -1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        # 4. find max area
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, (rightMost[i] - leftMost[i] +1) * heights[i])

        return maxArea