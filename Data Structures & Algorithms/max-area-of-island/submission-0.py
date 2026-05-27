class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1],[1, 0],[-1, 0],[0, -1]]
        ymax = len(grid)
        xmax = len(grid[0])
        maxArea = 0
        self.currArea = 0

        def valid(y, x):
            if y >= 0 and y < ymax and x >= 0 and x < xmax:
                return True
            else:
                return False

        def dfs(y, x):
            if not valid(y, x):
                return
            if grid[y][x] == 1:
                self.currArea += 1
                grid[y][x] = 0
                for direction in directions:
                    newY = y + direction[0]
                    newX = x + direction[1]
                    if valid(newY, newX):
                        dfs(newY, newX)

        for yy in range(ymax):
            for xx in range(xmax):
                dfs(yy, xx)
                maxArea = max(maxArea, self.currArea)
                self.currArea = 0
        
        return maxArea
