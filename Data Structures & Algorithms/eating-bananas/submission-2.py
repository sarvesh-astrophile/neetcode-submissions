class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r
        while l <= r:
            k = l + (r - l) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)

            if totalTime <= h:
                result = k
                r = k - 1
            else:
                l = k + 1

        return result
