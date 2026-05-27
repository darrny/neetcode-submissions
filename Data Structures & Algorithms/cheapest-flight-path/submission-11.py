class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float("inf")] * n
        cost[src] = 0

        for i in range(k + 1):
            tempCost = cost.copy()

            for src2, dst2, prc2 in flights:
                if cost[src2] == float("inf"):
                    continue
                if cost[src2] + prc2 < tempCost[dst2]:
                    tempCost[dst2] = cost[src2] + prc2
            cost = tempCost

        return -1 if cost[dst] == float("inf") else cost[dst]