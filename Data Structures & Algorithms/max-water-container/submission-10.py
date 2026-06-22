class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxC = 0

        l, r = 0, len(heights) -1
        while l < r:
            length = r - l
            cap = length * min(heights[l], heights[r])
            maxC = max(cap, maxC)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxC