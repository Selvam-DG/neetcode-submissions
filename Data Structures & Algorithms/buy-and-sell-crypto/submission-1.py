class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            buy_price = prices[i]
            for j in range(i+1, len(prices)):
                if prices[i] > prices[j]:
                    continue
                else:
                    sell_price = prices[j]
                    profit = sell_price-buy_price
                    max_profit = max(max_profit, profit)
        return max_profit
        