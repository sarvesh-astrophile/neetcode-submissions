class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        maxC = 0

        while l < r:
            if maxR > maxL:
                l += 1
                maxL = max(maxL, height[l])
                maxC += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                maxC += maxR - height[r]

        return maxC
        