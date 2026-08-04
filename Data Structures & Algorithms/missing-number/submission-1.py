class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        trivially: iterate through and figure out which one doesn't match
        ^ only works if sorted, which it's not.

        hashset works, iterate through
        """
        seen = set(nums)
        for i in range(len(nums)):
            if i not in seen:
                return i
        
        return len(nums)