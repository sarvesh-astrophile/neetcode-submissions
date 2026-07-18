class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #left
        stack = []
        leftMost = [-1] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                leftMost[i] = stack[-1]

            stack.append(i)

        #right
        stack = []
        rightMost = [len(heights)] * len(heights)
        for i in range(len(heights) -1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                rightMost[i] = stack[-1]

            stack.append(i)

        maxArea = 0
        for i in range(len(heights)):
            rightMost[i] -= 1
            leftMost[i] += 1
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))

        return maxArea