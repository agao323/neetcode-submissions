class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        go through and find all the indices of the original 0s
        go through again and mark all 0s for those rows and cols
        """
        first_row, first_col = False, False
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        first_row = True

                    if j > 0:
                        matrix[0][j] = 0
                    else:
                        first_col = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0
        
        if first_row:
            for j in range(cols):
                matrix[0][j] = 0