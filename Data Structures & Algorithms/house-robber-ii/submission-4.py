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

        def helper(nums):
            # rob_curr: best up to i - 2
            # do_not_rob: best up to i - 1
            rob_curr, do_not_rob = 0, 0

            for i in range(len(nums)):
                new_rob = max(rob_curr + nums[i], do_not_rob)
                rob_curr = do_not_rob
                do_not_rob = new_rob

            return do_not_rob
        
        return max(helper(nums[1:]), helper(nums[:-1]))
