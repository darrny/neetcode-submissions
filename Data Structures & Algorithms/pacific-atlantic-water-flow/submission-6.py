class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        atlantic = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        X, Y = len(heights[0]), len(heights)

        def dfs(x, y, grid):
            if grid[y][x]:
                return

            grid[y][x] = True

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if (
                    0 <= new_x < X
                    and 0 <= new_y < Y
                    and heights[new_y][new_x] >= heights[y][x]
                ):
                    dfs(new_x, new_y, grid)


        for x in range(X):
            dfs(x, 0, pacific)

        for y in range(Y):
            dfs(0, y, pacific)

        for x in range(X):
            dfs(x, Y - 1, atlantic)

        for y in range(Y):
            dfs(X - 1, y, atlantic)

        res = []
        for x in range(X):
            for y in range(Y):
                if atlantic[y][x] and pacific[y][x]:
                    res.append([y, x])

        return res