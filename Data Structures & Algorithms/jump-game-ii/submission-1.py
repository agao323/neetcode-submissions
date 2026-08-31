class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        maintain a high water mark, ie farthest right we can go
        scan through the array

        anytime the high water mark increases, increment by 1

        keep going until we reach len(nums) - 1
        """
        if len(nums) <= 1:
            return 0

        right = 0
        result = 0
        for i in range(len(nums)):
            cur = i + nums[i]
            if cur > right:
                result += 1
                right = cur
            if cur >= len(nums) - 1:
                return result

        return result