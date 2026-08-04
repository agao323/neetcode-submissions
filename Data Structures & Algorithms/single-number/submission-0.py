class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Obvious solution is hashset, but requires O(1) extra space.

        xor everything, gives you the unique number
        """
        result = 0

        for num in nums:
            result ^= num
        
        return result
        