class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        low = prices[0]
        for price in prices:
            if price < low:
                low = price
            if (price - low) > diff:
                diff = price - low
        return diff