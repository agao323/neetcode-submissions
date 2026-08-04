class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0
        lowest_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] - lowest_price > highest_profit:
                highest_profit = prices[i] - lowest_price
            if prices[i] < lowest_price:
                lowest_price = prices[i]
        
        return highest_profit
