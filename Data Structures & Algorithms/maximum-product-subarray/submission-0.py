class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        TIME:
            1:00:26 - had to look at and understand the solution for this one.
                      not sure if I even fully understand it still
                      
        product resets at 0, which we need to be careful about
        negative values are fine as long as there are an even amount

        can we ever have a max product be in the middle?
            yes, but only if it's surrounded by 0s, ie
            [100, 0, 12, 12, 0, 100]
            [-2, -10, -10, 0, 9, 9, 0, 99]
        
        because max product subarray will always be better if we include
        a positive value or even number of negative values, we don't
        need to check all the subarray possibilities in the middle

        because the biggest negative value can become the biggest
        positive value at any point we encounter another negative,
        we should track that along with the biggest positive values

        algo:
            initialize result, currMin, currMax
            go through array
                track the min and max and global result
                min can become max bc of negative * negative
            return the global result
        """

        min_product, max_product = 1, 1
        result = nums[0]

        for num in nums:
            if num < 0:
                max_product, min_product = min_product, max_product
            max_product = max(num * max_product, num)
            min_product = min(num * min_product, num)
            result = max(result, max_product)
        
        return result
        

