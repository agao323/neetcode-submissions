from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        logic:
        - use sets to track each row, column, and 3x3
        - don't think there's much more to optimize?
        - slight optimizations: 
            - skip any empty row/column/box
            - skip any with only one value
        """

        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                digit = board[i][j]
                if digit == '.':
                    continue

                if digit in rows[i]:
                    return False
                if digit in columns[j]:
                    return False
                k = ((i // 3), (j // 3))
                if digit in boxes[k]:
                    return False
                
                rows[i].add(digit)
                columns[j].add(digit)
                boxes[k].add(digit)

        return True