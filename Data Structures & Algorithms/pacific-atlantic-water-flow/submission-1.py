class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        initial thoughts:
            - run bfs from every cell
            - figure out if it can hit top or left, and bottom or right
            - if yes, add to results
            - can we make this more efficient?
        
        optimized:
            - run bfs from oceans
                - top and left, bottom and right
            - separate ocean grids to mark if reachable or not
            - go through and return where both are reachable

        [
            [1,2,3],
            [8,9,4],
            [7,6,5]
        ]

        """
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # pacific stuff
        pacific = [[0] * len(heights[0]) for _ in heights]
        pacific_queue = deque(
            [(0, j, heights[0][j]) for j in range(len(heights[0]))] + 
            [(i, 0, heights[i][0]) for i in range(len(heights))]
        )
        pacific_seen = set(
            [(a, b) for a, b, h in pacific_queue]
        )
        while pacific_queue:
            i, j, height = pacific_queue.popleft()
            pacific[i][j] = 1
            pacific_seen.add((i, j))

            for dx, dy in dirs:
                next_x = i + dx
                next_y = j + dy

                if (
                    0 <= next_x < rows
                    and 0 <= next_y < cols
                    and heights[next_x][next_y] >= heights[i][j]
                    and (next_x, next_y) not in pacific_seen
                ):
                    pacific_queue.append((next_x, next_y, heights[next_x][next_y]))

        # atlantic stuff
        atlantic = [[0] * len(heights[0]) for _ in heights]
        bottom = rows - 1
        right = cols - 1
        atlantic_queue = deque(
            [(bottom, j, heights[bottom][j]) for j in range(cols)] +
            [(i, right, heights[i][right]) for i in range(rows)]
        )
        atlantic_seen = set(
            [(a, b) for a, b, h in atlantic_queue]
        )

        while atlantic_queue:
            i, j, height = atlantic_queue.popleft()
            atlantic[i][j] = 1
            atlantic_seen.add((i, j))

            for dx, dy in dirs:
                next_x = i + dx
                next_y = j + dy

                if (
                    0 <= next_x < rows
                    and 0 <= next_y < cols
                    and heights[next_x][next_y] >= heights[i][j]
                    and (next_x, next_y) not in atlantic_seen
                ):
                    atlantic_queue.append((next_x, next_y, heights[next_x][next_y]))

            # if (i - 1 >= 0
            #     and heights[i - 1][j] >= heights[i][j] 
            #     and (i - 1, j) not in atlantic_seen):
            #     atlantic_queue.append((i - 1, j, heights[i - 1][j]))
            
            # if (j - 1 >= 0
            #     and heights[i][j - 1] >= heights[i][j]
            #     and (i, j - 1) not in atlantic_seen):
            #     atlantic_queue.append((i, j - 1, heights[i][j - 1]))

        # print(pacific)
        # print(atlantic)
        result = []

        for i in range(rows):
            for j in range(cols):
                # print(f"i, j, pacific[i][j]: {i}, {j}, {pacific[i][j]}")
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])


        return result