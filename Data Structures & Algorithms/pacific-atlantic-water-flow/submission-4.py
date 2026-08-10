class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        TIME:
            33:01.72
                implementation took too long

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

        pacific = [[0] * len(heights[0]) for _ in heights]
        atlantic = [[0] * len(heights[0]) for _ in heights]

        pacific_queue = deque(
            [(0, j, heights[0][j]) for j in range(len(heights[0]))] + 
            [(i, 0, heights[i][0]) for i in range(len(heights))]
        )
        self.bfs(heights, pacific_queue, pacific)

        bottom, right = len(heights) - 1, len(heights[0]) - 1
        atlantic_queue = deque(
            [(bottom, j, heights[bottom][j]) for j in range(len(heights[0]))] +
            [(i, right, heights[i][right]) for i in range(len(heights))]
        )
        self.bfs(heights, atlantic_queue, atlantic)

        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        
        print(pacific)
        print(atlantic)

        return result

    def bfs(self, heights, queue, output):
        rows, cols = len(heights), len(heights[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        seen = set([(a, b) for a, b, _ in queue])

        while queue:
            i, j, height = queue.popleft()
            output[i][j] = 1
            seen.add((i, j))

            for dx, dy in dirs:
                next_x = i + dx
                next_y = j + dy

                if (
                    0 <= next_x < rows
                    and 0 <= next_y < cols
                    and heights[next_x][next_y] >= heights[i][j]
                    and (next_x, next_y) not in seen
                ):
                    queue.append((next_x, next_y, heights[next_x][next_y]))
