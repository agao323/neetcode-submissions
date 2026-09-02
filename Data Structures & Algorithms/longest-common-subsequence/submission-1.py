class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        TIME:
            1:01:44 - learning 2D dp

        2D array, pad 0s for first row & col
        iterate through the array and establish recurrence relation:
            if text1[i - 1] == text2[j - 1] (match)
                [i][j] = 1 + [i - 1][j - 1]
            else:
                [i][j] = max([i - 1][j], [i][j - 1])
        return array[-1][-1]
        """
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]