class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        buy = prices[0]

        for price in prices:
            buy = min(buy, price)
            profit = price - buy
            maxprof = max(maxprof, profit)
        return maxprof
        