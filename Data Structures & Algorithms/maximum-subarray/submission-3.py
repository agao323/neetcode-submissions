class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        TIME:
            39:36.79
                - need to be a little faster on this one,
                  required help from AI to think through the
                  algorithm fully. had some hiccups coding out
                  and accounting for all the edge cases at the
                  end too

        start with creating prefix sum arry:
            [2,-1,3,1,3,4,3,7]

        iterate through this array.
        at each point, track the smallest prefix sum
        we've encountered, and track what the curr element
        - the smallest sum would be. If it's positive, we
        keep smallest sum to 0, because we should always
        take a positive number.

        the largest result will give us the right answer
        """
        if not nums:
            return 0

        prefix_sums = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            prefix_sums.append(curr_sum)
        
        # print(prefix_sums)

        min_sum = 0
        res = prefix_sums[0]
        for ps in prefix_sums:
            res = max(res, ps - min_sum)
            min_sum = min(min_sum, ps)
        
        return res

