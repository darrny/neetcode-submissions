class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r = len(word1) + 1
        c = len(word2) + 1
        grid = [[float("inf")] * c for _ in range(r)]

        for i in range(r):
            grid[i][c - 1] = r - 1 - i
        for i in range(c):
            grid[r - 1][i] = c - 1 - i
        
        for rr in range(r - 2, -1, -1):
            for cc in range(c - 2, -1 , -1):
                if word1[rr] == word2[cc]:
                    grid[rr][cc] = grid[rr + 1][cc + 1]
                else:
                    grid[rr][cc] = 1 + min(min(grid[rr + 1][cc], grid[rr][cc + 1]), grid[rr + 1][cc + 1])
        
        return grid[0][0]