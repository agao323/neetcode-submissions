class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        intuitively:
        - multiple everything together, get a total
        - go back through again, divide by nums[i]
        - O(2n)
        - notes: easily could hit integer overflow
        """
        num_zeros = 0

        total = 1
        for n in nums:
            if n == 0:
                num_zeros += 1
            else:
                total *= n

        
        result = [0] * len(nums)
        if num_zeros > 1:
            return result

        for i in range(len(result)):
            if nums[i] == 0:
                result[i] = total
            elif num_zeros == 1:
                result[i] = 0
            else:
                result[i] = int(total / nums[i])
        
        return result
        