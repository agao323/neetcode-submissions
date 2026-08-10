class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        keep dp array
        each element i in dp array is:
            max(don't rob current house, rob current house)
            where:
                don't rob = dp[i - 1]
                rob = dp[i - 2] + dp[i]
            return last element
        """
        # first two are dummy
        dp = [0] * (len(nums) + 2)
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])
        
        return dp[-1]