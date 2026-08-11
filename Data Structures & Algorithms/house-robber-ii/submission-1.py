class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        same thing as house robber I, but you can't rob the first and last houses

        so same implementation but dp array is len(nums) - 1? but then that doesn't
        even check the last house. use two dp arrays of len(nums) - 1? that should
        work but maybe not the most efficient
        """
        if len(nums) <= 2:
            return max(nums)

        dp1 = [0] * (len(nums) + 2)
        dp2 = [0] * (len(nums) + 2)

        for i in range(2, len(dp1) - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i - 2])

        for j in range(3, len(dp2)):
            dp2[j] = max(dp2[j - 1], dp2[j - 2] + nums[j - 2])

        print(dp1)
        print(dp2)
        
        return max(max(dp1), max(dp2))