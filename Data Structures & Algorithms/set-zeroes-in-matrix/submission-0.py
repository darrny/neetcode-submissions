class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        I, J = len(matrix), len(matrix[0])

        for i in range(I):
            for j in range(J):
                if matrix[i][j] == 0:
                    matrix[i][j] = None

        for i in range(I):
            for j in range(J):
                if matrix[i][j] is None:
                    for ii in range(I):
                        if matrix[ii][j] is not None:
                            matrix[ii][j] = 0
                    for jj in range(J):
                        if matrix[i][jj] is not None:
                            matrix[i][jj] = 0
        for i in range(I):
            for j in range(J):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
