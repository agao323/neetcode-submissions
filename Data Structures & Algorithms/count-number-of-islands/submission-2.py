class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    q = [[i,j]]
                    while q:
                        x,y = q.pop(0)
                        # check up
                        if 0 <= x-1 and grid[x-1][y] == '1':
                            q.append([x-1,y])
                            
                        # check down
                        if x+1 < len(grid) and grid[x+1][y] == '1':
                            q.append([x+1,y])

                        # check left
                        if 0 <= y-1 and grid[x][y-1] == '1':
                            q.append([x,y-1])

                        # check right
                        if y+1 < len(grid[0]) and grid[x][y+1] == '1':
                            q.append([x,y+1])

                        grid[x][y] = '0'
                    num += 1

        return num