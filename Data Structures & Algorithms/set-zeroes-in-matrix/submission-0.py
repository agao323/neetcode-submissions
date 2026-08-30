class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        go through and find all the indices of the original 0s
        go through again and mark all 0s for those rows and cols
        """
        zeroes = set()
        rows, cols = range(len(matrix)), range(len(matrix[0]))

        for i in rows:
            for j in cols:
                if matrix[i][j] == 0:
                    zeroes.add((i, j))
        
        row_indices = set([i for i, _ in zeroes])
        col_indices = set([j for _, j in zeroes])

        for i in rows:
            for j in cols:
                if i in row_indices or j in col_indices:
                    matrix[i][j] = 0
        
        