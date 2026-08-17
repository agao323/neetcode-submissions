class Solution:
    def numDecodings(self, s: str) -> int:
        """
        TIME: 
            1:14:37.23
                - really bad. used AI heavily to help solve, was 90% of the
                  way there but didn't get the case where I had to reset
                  current count back to 0 if the curr digit was a 0, since
                  there's only one possible valid encoding if curr digit is
                  0. So we have to just take dp[i - 2] instead of also
                  adding the possible ways from dp[i - 1].

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

        """ trying decode ways starting from the end

        "1012"

        dp[i + 1] is always set equal to dp[i + 2]
        because one digit doesn't add any new ways
        to decode. But once we see a double digit pair
        is valid to decode two different ways, we
        "double" the branching paths on each already
        valid way to decode, and mimick this "doubling"
        by adding dp[i + 1] and dp[i + 2]

        XX
            X > 26 -> one valid way
            26 >= X >= 10
                dp[i + 1] + dp[i + 2]
                single & double digit cases are both
                valid so add them to all the possible
                ways we've already found before
        00 -> invalid, return 0
        X0
            X > 2 -> invalid, return 0
            X == {1,2} -> one valid way, which
                          doesn't increment the total
                          number of valid ways
        0X -> invalid, but could be later
            keep going but take dp[i + 2]

        """
        if not s or s[0] == '0':
            return 0
        
        # add one to accommodate base case of empty string,
        # which has 1 valid way of decoding (nothing)
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if i == len(s) - 1:
                dp[i] = 1
                continue
            
            first, second = int(s[i]), int(s[i + 1])
            both = int(s[i] + s[i + 1])
            count = dp[i + 1]

            if (first > 2 and second == 0) or both == 0:
                return 0
            
            if 10 <= both <= 26:
                count += dp[i + 2]
            
            if first == 0 and second > 0:
                count = 0
                
            dp[i] = count

        return dp[0]
            

        """
        if not s or s[0] == '0':
            return 0

        dp = [0] * len(s)
        dp[0] = 1

        for i in range(1, len(s)):
            curr, prev = int(s[i]), int(s[i - 1])
            both = int(s[i - 1] + s[i])
            prev_count = dp[i - 2] if i > 1 else 1

            if (prev == 0 and curr == 0) or (prev > 2 and curr == 0):
                return 0

            curr_count = dp[i - 1] if curr != 0 else 0   # only inherit if single-digit is valid
            if 10 <= both <= 26:                          # double-digit check, independent of curr
                curr_count += prev_count

            dp[i] = curr_count

        # print(dp)

        return dp[-1]
        """


