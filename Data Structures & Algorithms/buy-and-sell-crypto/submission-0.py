class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            bp = prices[i]
            for j in range(i+1, len(prices)):
                sp = prices[j]
                res = max(res, sp-bp)
        return res    

        