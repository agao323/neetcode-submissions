class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        TIME:
            14:19.98
                - finished naive slow dfs solution
            34:14.42
                - finished O(n) solution

        can jump backwards
        can jump any number of steps

        initial thoughts:
            - dfs through the possible paths, which is jump forward or jump back
            - base case: curr index < 0 or >= len(nums), we're out of bounds
                return False
            - base case: curr index == len(nums) - 1
                return True
            - dfs(curr - curr[i]), dfs(curr + curr[i])
        """


        """ dp maybe?

        track separate dp array of len(nums)
        at each point we track the farthest reachable spot
        if we encounter a number that increases it, we update
        the farthest reachable spot
        when we can't move anymore, figure out if we're at or
        past the end

        so for the examples:
            [1,2,0,1,0]
            farthest = 1 -> 3 -> 3 -> 4
            [1,2,1,0,1]
            farthest = 1 -> 3 -> 3 -> done
            [1,0,3,1,0,0]
            farthest = 1 -> done
            [1,2,3,1,0,0]
            farthest = 1 -> 3 -> 6

            if our index > farthest, we're done. can't reach
            anymore spots
        """

        # goal = len(nums) - 1

        # for i in range(len(nums) - 2, -1, -1):
        #     if i + nums[i] >= goal:
        #         goal = i
        
        # return goal == 0

        farthest = 0
        for i in range(len(nums)):
            if farthest < i:
                return False
            farthest = max(farthest, i + nums[i])
        return True

        """
        seen = set()

        def dfs(i):
            if i in seen:
                return False
            seen.add(i)
            if i >= len(nums) - 1:
                return True
            if i < 0 or nums[i] == 0:
                return False
            
            results = [
                dfs(j) for j in range(i - nums[i], i + nums[i] + 1)
            ]
            return any(results)
            
        
        return dfs(0)
        """