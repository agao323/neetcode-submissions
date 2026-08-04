class Solution:
    def isHappy(self, n: int) -> bool:
        """
        1. Compute the squares of all digits
        2. Track all seen numbers in a set
        3. Keep going until we hit 1 or a number we've already seen
        """

        seen = set()

        while n != 1:
            n = self.sumSquares(n)
            if n in seen:
                return False
            seen.add(n)
            
        return True

    def sumSquares(self, n: int) -> int:
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit ** 2
            n = n // 10
        return sum