class Solution:
    def reverseBits(self, n: int) -> int:
        """
        TIME: 6:34.29

        logic:
        - turn into string, reverse, return as binary
        """

        # n_str = bin(n)[::-1]
        # cleaned = n_str[:-2]
        # result = cleaned + ''.join('0' for _ in range(32 - len(cleaned)))
        # return int(result, base=2)

        # makes more sense to do this with proper bit manipulation
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += bit << (31 - i)
        return res