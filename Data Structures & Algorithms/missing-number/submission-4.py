class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        TIME: 18:17.19
        
        trivially: iterate through and figure out which one doesn't match
        ^ only works if sorted, which it's not.

        hashset works, iterate through
        O(1) space complexity:
        - xor everything in nums with index
        - xor last number, the biggest one
        - remainder is the missing number
        """
        res = 0
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        res ^= len(nums)
        return res

