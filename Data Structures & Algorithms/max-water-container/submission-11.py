class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        l, r = 0, len(heights) -1
        while l < r:
            length = r - l
            if heights[l] > heights[r]:
                maxW = max(maxW, heights[r] * length)
                r -= 1
            else:
                maxW = max(maxW, heights[l] * length)
                l += 1

        return maxW