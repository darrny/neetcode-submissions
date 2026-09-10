class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0 for n in range(n)] for m in range(m)]

        for nn in range(n):
            ways[0][nn] = 1
        for mm in range(m):
            ways[mm][0] = 1

        for mm in range(1, m):
            for nn in range(1, n):
                ways[mm][nn] = ways[mm - 1][nn] + ways[mm][nn - 1]

        return ways[-1][-1]