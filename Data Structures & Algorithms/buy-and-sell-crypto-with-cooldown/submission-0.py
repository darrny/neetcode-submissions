class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(index, buying):
            if index >= len(prices):
                return 0
            if (index, buying) in cache:
                return cache[(index, buying)]

            if buying:
                buy = dfs(index + 1, not buying) - prices[index]
                rest = dfs(index + 1, buying)
                cache[(index, buying)] = max(buy, rest)
            if not buying:
                sell = dfs(index + 2, not buying) + prices[index]
                rest = dfs(index + 1, buying)
                cache[(index, buying)] = max(sell, rest)
            return cache[(index, buying)]
        
        return dfs(0, True)