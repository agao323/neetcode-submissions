class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        TIME: 7:33.15

        had to look this up:
        - >> is the operator to shift right one
        - & with 1 will tell us if the last bit is a 1

        so:
        - go through every bit, & with 1
        - count number of times that gives us a 1
        - loop through all bits

        optimal:
        - n & (n - 1), count number of iterations that happens
        - ie n = 1000, n - 1 = 0111
        - all the 1 bits get eliminated from this AND operation
        """
        # count = 0
        # while n:
        #     if n & 1 == 1:
        #         count += 1
        #     n >>= 1
        # return count

        # optimal solution:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count