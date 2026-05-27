class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerL = 0
        outerR = len(matrix) - 1
        outerM = 0

        while outerL <= outerR:
            outerM = (outerL + outerR) // 2
            if matrix[outerM][0] == target:
                return True
            elif matrix[outerM][0] < target:
                outerL = outerM + 1
            else:
                outerR = outerM - 1
        if matrix[outerM][0] < target:
            r = outerM
        else:
            r = outerM - 1

        l = 0
        h = len(matrix[r]) - 1

        while l <= h:
            m = (l + h) // 2
            if matrix[r][m] == target:
                return True
            elif matrix[r][m] > target:
                h = m - 1
            else:
                l = m + 1
        
        return False