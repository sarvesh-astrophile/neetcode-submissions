class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
            
        maxL = height[0]
        maxR = height[len(height) - 1]
        result = 0

        l, r = 0, len(height) - 1
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL) 
                result += max(min(maxL, maxR) - height[l], 0)
            else:
                r -= 1
                maxR = max(height[r], maxR)
                result += max(min(maxL, maxR) - height[r], 0)

        return result