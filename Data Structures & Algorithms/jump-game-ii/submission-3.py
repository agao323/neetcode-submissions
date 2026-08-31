class Solution:
    def jump(self, nums: List[int]) -> int:
        """
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

        dp = [0] * len(nums)
        farthest = [0] * len(nums)
        for i in range(len(nums)):
            farthest[i] = i + nums[i]
        
        result = 0
        goal = len(farthest) - 1
        while goal > 0:
            # print(farthest)
            for i in range(len(farthest)):
                if farthest[i] >= goal:
                    farthest = farthest[:i + 1]
                    break
            result += 1
            goal = len(farthest) - 1

        return result

