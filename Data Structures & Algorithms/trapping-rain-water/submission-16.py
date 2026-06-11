class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        maxCap = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                cap = min(maxL, maxR) - height[l]
                maxCap += max(cap, 0)
            else:
                r -= 1
                maxR = max(maxR, height[r])
                cap = min(maxL, maxR) - height[r]
                maxCap += max(cap, 0)

        return maxCap

