class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Approaches:
            1. Backtracking
            2. DP array
                - because leading zeros are invalid, we could go from right
                  to left and track the possible combinations that way
                - actually, as long as the string starts with a zero, it will
                  always be invalid
                - same thing applies for anything greater than 1 or 2 followed
                  by a zero. "30", "40", "50", etc. will never be valid
        
        algo:
            - if first char is 0, return 0
            - initialize dp array with first element = 1 possible way
            - go through the string from 1 to len(s)
            - if s[i] > 0, add one. then look at s[i-1] + s[i]
                - if s[i-1] is 0, don't do anything
                - if s[i-1] + s[i] > 26, don't do anything
                - otherwise, add one to the count at dp[i]
                - all cases:
                    - XX, 0X, X0, 00
            - return the last element

        "1012"
            "10, 1, 2"
            "10, 12"
        
        test cases:
            - empty string
            - "0", "00", "00000000"
            - "00001"
            - "999999"
            - "262626262627"
            - "1000"
            - "102"
        """
        if not s or s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            curr, prev = int(s[i - 1]), int(s[i - 2])
            # print(f"curr: {curr}, prev: {prev}")
            both = int(s[i - 2] + s[i - 1])
            prev_count = dp[i - 1]

            if ((prev == 0 and curr == 0) or
                (prev > 2 and curr == 0)):
                return 0

            if prev > 0 and curr > 0:
                if both <= 26:
                    prev_count += dp[i - 2]
                # else:
                    # prev_count += 1
            
            dp[i] = prev_count
        
        # print(dp)
                
        return dp[-1]


