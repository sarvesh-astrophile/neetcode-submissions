class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0

        i, j = 0, len(heights) - 1
        while j > i:
            distance = j - i
            height = min(heights[i], heights[j])

            if largest < (distance * height):
                largest = distance * height

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
                
        return largest

