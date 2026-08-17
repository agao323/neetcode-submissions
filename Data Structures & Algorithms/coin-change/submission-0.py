class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        1D dp problem

        we initialize an array of size <amount>
        going through the array from 0 to amount - 1, we can try
        subtracting each denomination of coin. initialize the array
        with 0 set to 1 to represent that we can make an amount 0
        from 0 coins.
        
        then when curr - coin == 0, we know we can reach curr with 
        the set of denominations. math should be (curr index + 1) - coin == 0.

        at that point if it's 0, set it to whatever value we have.
        the default value should be prev + 1.

        if it's not 0, take min(prev + 1, curr) in case we've hit that
        amount with some other denomination.

        This way we build it up until we get to amount, ie 5 + 5 + 10
        = 20, set that to 3. but 5 + 5 + 5 + 5 is 4, so we keep it to 3.

        return dp[-1] if > 0 else -1.

        Test cases:
            - adds up correctly
                - multiple possible cases still returns the minimum
            - does not add up
                - returns -1
            - no coins, amount > 0 / amount == 0
            - no amount, no coins / yes coins

        O(n*m) time, n = amount, m = # of coins
        O(n) space
        """

        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for c in coins:
                if i - c < 0:
                    continue
                
                prev = dp[i - c]
                # print(f"prev: {prev}")
                if prev == -1:
                    continue
                else:
                    if dp[i] == -1:
                        dp[i] = prev + 1
                        # print(dp[i])
                    else:
                        dp[i] = min(dp[i], prev + 1)
        print(dp)
        
        return dp[-1]

                    

