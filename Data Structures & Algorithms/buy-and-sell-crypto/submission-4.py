class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maximum_profit = 0

        for price in prices:
            if price < lowest:
                lowest = price
            if price - lowest > maximum_profit:
                maximum_profit = price - lowest
        
        return maximum_profit