class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, visit, currHeight):
            if min(r, c) < 0 or r >= rows or c >= cols or (r, c) in visit or heights[r][c] < currHeight:
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])


        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        res = []
        for r, c in atlantic:
            if (r, c) in pacific:
                res.append([r, c])
        return res
