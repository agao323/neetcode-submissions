class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        two pass approach:
            keep a visited & captured set of indicies {(i1, j1), (i2, j2), etc.}
            every time we encounter a new region, we figure out if it should
            be captured or not
            if we want to capture
                add to captured set of indices
            if not
                add to visited set of indicies
            ignore any index that's already in one or the other
            change all captured indices to X
        
        time: O(m * n)
        space: O(m * n)
        """
        if not board:
            return

        visited, captured = set(), set()
        rows, cols = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                cur = (i, j)
                if (
                    cur in visited 
                    or cur in captured 
                    or board[i][j] == 'X'
                ):
                    continue
                
                queue = deque([(i, j)])
                cur_region = set([(i, j)])
                should_capture = True
                while queue:
                    x, y = queue.popleft()

                    # edge of board
                    if (
                        x == 0 or x == rows - 1 
                        or y == 0 or y == cols - 1
                    ):
                        should_capture = False

                    # keep going to explore the entire region
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < rows 
                            and 0 <= ny < cols
                            and board[nx][ny] == 'O'
                            and (nx, ny) not in cur_region
                        ):
                            queue.append((nx, ny))
                            cur_region.add((nx, ny))
                
                # finished exploring region, add to one of the sets
                if should_capture:
                    captured |= cur_region
                else:
                    visited |= cur_region
        
        for i, j in captured:
            board[i][j] = 'X'









                    
