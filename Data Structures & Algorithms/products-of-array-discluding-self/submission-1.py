class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        TIME: 12:50.19 to solve initial intuitive solution handling edge cases with 0s

        intuitively:
        - multiple everything together, get a total
        - go back through again, divide by nums[i]
        - O(2n)
        - notes: easily could hit integer overflow

        O(n) solution without division:
        - multiply from left to right, not including curr
        - multiply from right to left, not including curr
        """
        if len(nums) <= 1:
            return nums

        result = list(nums)

        curr_product = nums[0]
        for i in range(1, len(nums)):
            result[i] = curr_product
            curr_product *= nums[i]
        
        curr_product = nums[-1]
        for j in range(len(nums) - 2, -1, -1):
            result[j] = curr_product * result[j]
            curr_product *= nums[j]
        return result



        # num_zeros = 0

        # total = 1
        # for n in nums:
        #     if n == 0:
        #         num_zeros += 1
        #     else:
        #         total *= n

        # result = [0] * len(nums)
        # if num_zeros > 1:
        #     return result

        # for i in range(len(result)):
        #     if nums[i] == 0:
        #         result[i] = total
        #     elif num_zeros == 1:
        #         result[i] = 0
        #     else:
        #         result[i] = int(total / nums[i])
        
        # return result
        