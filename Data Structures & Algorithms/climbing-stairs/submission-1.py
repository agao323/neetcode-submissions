class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        num_ways = [1, 2] + [0] * (n - 2)

        for i in range(2, len(num_ways)):
            num_ways[i] = num_ways[i - 1] + num_ways[i - 2]

        return num_ways[-1]
        