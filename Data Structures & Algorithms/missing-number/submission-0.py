class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        trivially: iterate through and figure out which one doesn't match
        """
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)