class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        #leftMost
        leftMost = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                leftMost[i] = stack[-1]

            stack.append(i)

        #righMost
        rightMost = [n] * n
        stack = []
        for i in range(n -1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                rightMost[i] = stack[-1]

            stack.append(i)

        #final
        maxArea = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, (rightMost[i] - leftMost[i] + 1) * heights[i])

        return maxArea