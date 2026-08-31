class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        TIME:
            48:51 - took way to long again.. need to figure out
                    a more algorithmic way of approaching these
                    greedy problems

        maintain a high water mark, ie farthest right we can go
        scan through the array

        anytime the high water mark increases, increment by 1
        we need to be careful here though. we should track
        the farthest we can go with the least amount of jumps
        before we actual increment by 1, which guarantees
        we're going as far as we can

        keep going until we reach len(nums) - 1


        build an array showing the farthest we can reach
        from every point

        iterate backwards and find the earliest element where
        we can reach the goal. 
        
        new goal is now that index. find the next earliest
        element that gets us to that goal.

        repeat until we reach the start, and return the number
        of times we repeated this process
        """

        jumps = 0
        l, r = 0, 0

        # keep going until we hit the end
        while r < len(nums) - 1:
            # go through window [l, r] and figure out
            # the maximum distance we can jump to, and
            # assign that to r
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            # start looking in the next window, everything
            # up until r has been check so we go to r + 1
            l = r + 1
            r = farthest

            # increment jumps
            jumps += 1


        return jumps


        """
        farthest = [0] * len(nums)
        for i in range(len(nums)):
            farthest[i] = i + nums[i]
        
        result = 0
        goal = len(farthest) - 1
        while goal > 0:
            for i in range(len(farthest)):
                if farthest[i] >= goal:
                    farthest = farthest[:i + 1]
                    break
            result += 1
            goal = len(farthest) - 1

        return result
        """
