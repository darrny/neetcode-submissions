class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        X, Y = len(board[0]), len(board)
        seen = set()

        def dfs(x, y, i):
            if i == len(word):
                return True
            
            if x < 0 or x >= X or y < 0 or y >= Y or (x, y) in seen or board[y][x] != word[i]:
                return False

            seen.add((x, y))

            res = False

            for direction in DIRECTIONS:
                new_x, new_y = x + direction[0], y + direction[1]
                res = res or dfs(new_x, new_y, i + 1)

            seen.remove((x, y))
            return res

        for x in range(X):
            for y in range(Y):
                if dfs(x, y, 0):
                    return True
            
        return False