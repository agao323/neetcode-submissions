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
        """
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        # pacific stuff
        pacific = [[0] * len(heights[0]) for _ in heights]
        pacific_queue = deque(
            [(0, j, heights[0][j]) for j in range(len(heights[0]))] + 
            [(i, 0, heights[i][0]) for i in range(len(heights))]
        )
        pacific_seen = set([(i, j) for i, j, _ in pacific_queue])
        while pacific_queue:
            i, j, height = pacific_queue.popleft()
            pacific[i][j] = 1
            pacific_seen.add((i, j))

            if (i + 1 < rows
                and heights[i + 1][j] >= heights[i][j] 
                and (i + 1, j) not in pacific_seen):
                pacific_queue.append((i + 1, j, heights[i + 1][j]))
            
            if (j + 1 < cols
                and heights[i][j + 1] >= heights[i][j]
                and (i, j + 1) not in pacific_seen):
                pacific_queue.append((i, j + 1, heights[i][j + 1]))

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

            if (i - 1 >= 0
                and heights[i - 1][j] >= heights[i][j] 
                and (i - 1, j) not in atlantic_seen):
                atlantic_queue.append((i - 1, j, heights[i - 1][j]))
            
            if (j - 1 >= 0
                and heights[i][j - 1] >= heights[i][j]
                and (i, j - 1) not in atlantic_seen):
                atlantic_queue.append((i, j - 1, heights[i][j - 1]))

        # print(pacific)
        # print(atlantic)
        result = []

        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])


        return result