class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        row_start, row_end
        col_start, col_end

        directions: E -> S -> W -> N
        E: (row_start, col_start) -> (row_end, col_start), col_start += 1
        S: (row_end, col_start) -> (row_end, col_end), row_end -= 1
        W: (row_end, col_end) -> (row_start, col_end), col_end -= 1
        N: (row_start, col_end) -> (row_start, col_start), row_start += 1

        keep going while row_start < row_end and col_start < col_end
        """
        row_start, col_start = 0, 0
        row_end, col_end = len(matrix[0]) - 1, len(matrix) - 1

        result = []

        while True:
            # EAST
            for i in range(row_start, row_end + 1):
                result.append(matrix[col_start][i])
            col_start += 1
            if len(result) == len(matrix[0]) * len(matrix):
                break

            # SOUTH
            for i in range(col_start, col_end + 1):
                result.append(matrix[i][row_end])
            row_end -= 1
            if len(result) == len(matrix[0]) * len(matrix):
                break

            # WEST
            for i in range(row_end, row_start - 1, -1):
                result.append(matrix[col_end][i])
            col_end -= 1
            if len(result) == len(matrix[0]) * len(matrix):
                break

            # NORTH
            for i in range(col_end, col_start - 1, -1):
                result.append(matrix[i][row_start])
            row_start += 1
            if len(result) == len(matrix[0]) * len(matrix):
                break
                
        return result