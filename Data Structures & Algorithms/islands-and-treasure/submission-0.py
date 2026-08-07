from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        bfs algo:
            - go through and start from each treasure chest
            - increment distance by one each time we add to queue
            - only add an adjacent cell if the new distance is 
              smaller than what is currently in the grid
            - override any larger values with smaller ones
        """

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    continue
                
                q = deque([(i, j, 0)])
                while q:
                    x, y, dist = q.popleft()
                    grid[x][y] = dist

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        next_x = x + dx
                        next_y = y + dy

                        if (
                            0 <= next_x < rows
                            and 0 <= next_y < cols
                            and grid[next_x][next_y] != -1
                            and grid[next_x][next_y] > dist + 1
                        ):
                            q.append(
                                (next_x, next_y, dist + 1)
                            )

