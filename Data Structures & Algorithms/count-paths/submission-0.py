class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        initial thoughts:
            - initialize empty grid m x n
            - dp. move down and right, each cell is just
              paths stored in up and left cells + 1
        """

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        rows, cols = len(dp), len(dp[0])

        for i in range(rows):
            for j in range(cols):
                for di, dj in [(1, 0), (0, 1)]:
                    next_i = i + di
                    next_j = j + dj
                    if next_i < rows and next_j < cols:
                        dp[next_i][next_j] += dp[i][j]

        return dp[-1][-1]
        