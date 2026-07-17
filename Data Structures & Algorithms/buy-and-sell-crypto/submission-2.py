class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, diff = prices[0], 0
        for price in prices:
            if price - low > diff:
                diff = price - low
            if price < low:
                low = price
        return diff