class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        xx = len(grid[0])
        yy = len(grid)
        islands = 0

        def dfs(y, x):
            for direction in directions:
                if x + direction[0] >= 0 and x + direction[0] < xx and y + direction[1] >= 0 and y + direction[1] < yy:
                    if grid[y + direction[1]][x + direction[0]] == "1":
                        grid[y + direction[1]][x + direction[0]] = "0"
                        dfs(y + direction[1], x + direction[0])

        for i in range(xx):
            for j in range(yy):
                if grid[j][i] == "1":
                    islands += 1
                    dfs(j, i)

        return islands