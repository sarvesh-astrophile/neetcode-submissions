class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maximum = 0

        while i < j :
            distance = j - i
            capacity = min(heights[i], heights[j]) * distance
            maximum = max(maximum, capacity)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

            
        return maximum