class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        TIME: 
            7:03.42 - DP
            ~12:03.42 - DFS + memo
        
        keep dp array
        each element i in dp array is:
            max(don't rob current house, rob current house)
            where:
                don't rob = dp[i - 1]
                rob = dp[i - 2] + dp[i]
            return last element
        """

        """ dfs solution
        """
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        
        return dfs(0)

        """ dp solution

        # first two are dummy
        dp = [0] * (len(nums) + 2)
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])
        
        return dp[-1]
        """