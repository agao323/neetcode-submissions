class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        TIME:
            7:21.31 - bfs solution worked on first try, felt pretty good.
                      should come back and try DSU algo later

        BFS while tracking the ticks on the queue

        go through the grid, find any rotten fruit, add them to the queue
        with 0 representing the minutes

        add any adjacent fresh fruit, increment the minute counter, mark
        them as rotten at that minute

        keep going until we've exhausted all paths

        go through and check for any fresh fruit remaining
        """

        rows, cols = range(len(grid)), range(len(grid[0]))

        queue = []
        for r in rows:
            for c in cols:
                if grid[r][c] == 2:
                    queue.append((0, r, c))

        result = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            t, x, y = queue.pop(0)
            result = max(result, t)

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(rows):
                    if grid[nx][y] == 1:
                        queue.append((t + 1, nx, y))
                        grid[nx][y] = 2
                if 0 <= ny < len(cols):
                    if grid[x][ny] == 1:
                        queue.append((t + 1, x, ny))
                        grid[x][ny] = 2
            
        
        for r in rows:
            for c in cols:
                if grid[r][c] == 1:
                    return -1
        
        return result




