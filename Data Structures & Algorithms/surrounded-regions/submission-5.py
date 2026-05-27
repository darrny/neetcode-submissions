class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.rows, self.cols = len(board), len(board[0])

        def safe(r, c):
            if min(r, c) < 0 or r == self.rows or c == self.cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            safe(r + 1, c)
            safe(r - 1, c)
            safe(r, c + 1)
            safe(r, c - 1)

        for r in range(self.rows):
            safe(r, 0)
            safe(r, self.cols - 1)

        for c in range(self.cols):
            safe(0, c)
            safe(self.rows - 1, c)

        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
    