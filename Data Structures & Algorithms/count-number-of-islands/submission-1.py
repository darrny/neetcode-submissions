class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        count = 0
        X = len(grid[0])
        Y = len(grid)

        def dfs(x, y):
            if x < 0 or x >= X or y < 0 or y >= Y:
                return

            if grid[y][x] == '1':
                grid[y][x] = 0
                
                for xx, yy in DIRECTIONS:
                    dfs(x + xx, y + yy)
        
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == '1':
                    count += 1
                    dfs(x, y)

        return count