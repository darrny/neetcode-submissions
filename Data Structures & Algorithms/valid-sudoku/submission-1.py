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
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    column = (square % 3) * 3 + j
                    if board[row][column] == '.':
                        continue
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])
        
        return True
