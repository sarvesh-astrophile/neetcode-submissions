class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        l = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)

            if prices[l] > prices[r]:
                l = r

        return maxP
