class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        TIME:
            14:30.65 - finished implementation for initial thoughts

        same thing as house robber I, but you can't rob the first and last houses

        so same implementation but dp array is len(nums) - 1? but then that doesn't
        even check the last house. use two dp arrays of len(nums) - 1? that should
        work but maybe not the most efficient

        can we do this with a single dp array?
            - yes. just keep one array and do one pass forward, one pass backwards
        """
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        

        dp1 = [0] * len(nums)
        dp1[-1] = nums[-1]
        dp1[-2] = max(nums[-1], nums[-2])
        for j in range(len(nums) - 3, 0, -1):
            curr = max(dp1[j + 1], dp1[j + 2] + nums[j])
            dp1[j] = max(dp1[j], curr)

        return max(max(dp), max(dp1))
