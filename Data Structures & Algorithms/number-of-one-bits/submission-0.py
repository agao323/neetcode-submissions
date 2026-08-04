class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        had to look this up:
        - >> is the operator to shift right one
        - & with 1 will tell us if the last bit is a 1

        so:
        - go through every bit, & with 1
        - count number of times that gives us a 1
        - loop through all bits
        """
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count