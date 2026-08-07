class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        TIME
            10:56.46 - 2D dp array

        initial thoughts:
            - initialize empty grid m x n
            - dp. move down and right, each cell is just
              paths stored in up and left cells + 1
        """

        """ space optimized dp
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        
        return dp[-1]

        """ 2D matrix dp solution

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1

        rows, cols = len(dp), len(dp[0])
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
        """