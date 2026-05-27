class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        for square in range(9):
            row = square // 3
            col = square % 3
            seen = set()
            for i in range(3):
                for j in range(3):
                    if board[i + 3 * row][j + 3 * col] == '.':
                        continue
                    if board[i + 3 * row][j + 3 * col] in seen:
                        return False
                    seen.add(board[i + 3 * row][j + 3 * col])
        
        return True
