class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        TIME: 21:29.28
        
        brute force:
        - go through every number and count the number of bits
        - can efficiently count with bitwise n & (n - 1)

        optimized?
        - 101 is 5, 110 is 6, 111 is 7
        - 1000 is 8
        - 1110 is 14
        - 10000 is 16

        observations: 
        - every number at a power of 2 is 1
        - every number between powers of 2 can be made from:
            1. the previous power of 2
            2. adding a number before that
        - so, instead of counting the number of bits every time:
            - go through and set each power of 2 to 1
            - figure out each count with: number - (most recent pow of 2) + 1
        
        time complexity:
        - calculating powers of 2 is log(n)
        - iterating is O(n)
        - compared to calculating bits every time, which is O(n * m) or O(n * log(m))

        space:
        - O(n)
        """
        if n == 0:
            return [0]

        result = [0] * (n + 1)
        result[1] = 1
        powers_of_2 = set()

        power = 1
        while 2 ** power <= n:
            result[2 ** power] = 1
            powers_of_2.add(2 ** power)
            power += 1
        
        lowest_power_of_2 = 2
        for i in range(2, len(result)):
            # skip powers of 2
            if result[i] > 0:
                lowest_power_of_2 = i
                continue
            diff = i - lowest_power_of_2
            result[i] = result[diff] + 1
        
        return result


        