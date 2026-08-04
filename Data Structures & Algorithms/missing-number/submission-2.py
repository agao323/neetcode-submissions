class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        trivially: iterate through and figure out which one doesn't match
        ^ only works if sorted, which it's not.

        hashset works, iterate through
        O(1) space complexity:
        - new list nums that's complete
        - xor everything
        - remainder is the missing number
        """
        all_nums = [i for i in range(len(nums) + 1)]
        res = 0
        for num in nums:
            res ^= num
        for num in all_nums:
            res ^= num
        return res

