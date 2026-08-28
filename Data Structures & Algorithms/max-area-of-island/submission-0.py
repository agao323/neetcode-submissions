class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        go through the matrix
        if we encounter a 1, start a bfs
            flip all 1s to 0s so we don't recount islands
            maintain global largest island
        return global largest
        """

        rows, cols = len(grid), len(grid[0])
        result = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                result = max(result, self.bfs(grid, i, j))
        
        return result

    
    def bfs(self, grid, i, j) -> int:
        count = 0
        queue = [(i, j)]
        while queue:
            x, y = queue.pop(0)
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            grid[x][y] = 0

            for dx, dy in dirs:
                if 0 <= x + dx < len(grid) and grid[x + dx][y] == 1:
                    queue.append((x + dx, y))
                if 0 <= y + dy < len(grid[0]) and grid[x][y + dy] == 1:
                    queue.append((x, y + dy))

            count += 1

        return count            
