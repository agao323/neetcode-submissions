class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        TIME:
            13:12.57 - tripped up a bit on overcounting visited coordinates

        go through the matrix
        if we encounter a 1, start a bfs
            flip all 1s to 0s so we don't recount islands
            maintain global largest island
        return global largest

        grid=[
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,0,1,1],
            [0,0,0,1,1]
        ]

        """

        rows, cols = len(grid), len(grid[0])
        result = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue

                count = 0
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    grid[x][y] = 0
                    count += 1

                    for dx, dy in dirs:
                        if 0 <= x + dx < len(grid) and grid[x + dx][y] == 1:
                            queue.append((x + dx, y))
                            grid[x + dx][y] = 0
                        if 0 <= y + dy < len(grid[0]) and grid[x][y + dy] == 1:
                            queue.append((x, y + dy))
                            grid[x][y + dy] = 0

                result = max(result, count)
        
        return result
         
