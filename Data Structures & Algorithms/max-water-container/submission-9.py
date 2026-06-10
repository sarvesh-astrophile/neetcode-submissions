class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxC = 0

        while l < r:
            capacity = (r - l) * min(heights[l], heights[r])
            maxC = max(maxC, capacity)

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1


        return maxC