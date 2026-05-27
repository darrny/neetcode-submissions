class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])

        def add_cell(r, c):
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == 0:
                return
            q.append((r, c))
            visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        for i in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = 2
            add_cell(r + 1, c)
            add_cell(r - 1, c)
            add_cell(r, c + 1)
            add_cell(r, c - 1)

        time = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                add_cell(r + 1, c)
                add_cell(r - 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)
            time += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return time