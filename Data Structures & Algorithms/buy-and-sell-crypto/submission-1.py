class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ret = 0
        if n < 2:
            return 0

        l = 0
        r = l + 1

        while r < n:
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                ret = max(ret, profit)
                r += 1
        

        return ret