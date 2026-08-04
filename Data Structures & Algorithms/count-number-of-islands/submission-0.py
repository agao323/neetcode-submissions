class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    q = [[i,j]]
                    print(q)
                    while q:
                        x,y = q.pop(0)
                        # check up
                        if 0 <= x-1 and x-1 < len(grid) and 0 <= y and y < len(grid[0]) and grid[x-1][y] == '1':
                            q.append([x-1,y])
                            
                        # check down
                        if 0 <= x+1 and x+1 < len(grid) and 0 <= y and y < len(grid[0]) and grid[x+1][y] == '1':
                            q.append([x+1,y])

                        # check left
                        if 0 <= x and x < len(grid) and 0 <= y-1 and y-1 < len(grid[0]) and grid[x][y-1] == '1':
                            q.append([x,y-1])

                        # check right
                        if 0 <= x and x < len(grid) and 0 <= y+1 and y+1 < len(grid[0]) and grid[x][y+1] == '1':
                            q.append([x,y+1])

                        grid[x][y] = '0'
                    num += 1

        return num