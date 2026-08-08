import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        if len(piles) == h, must be the max in piles

        piles = [25,10,23,4], h = 4

        what if h = 5?
        then k = 23, because we can now split 25 into 23 + 2

        what if h = 6? -> total = 62 -> total / h = ~10.33
        does that mean k = 11?
            no, because we can't complete the bigger piles in time
        this implies that
            h - len(piles) = additional hours to split
            take the max pile and divide by that
            so in the example above, 25 / (6 - 4) = 12.5, round up to 13

        piles = [1,4,3,2], h = 9
        9 - 4 = 5 additional hours. 4 / 5 = 0.8, round up to 1
        that doesn't work.

        what insight can we derive from this?

        another way of framing this:
            - we have h - len(piles) dividers
            - what is the smallest k such that:
                - # items between every divider <= k
            - we DO NOT have to use every divider
            - we just have to make sure we don't run out of dividers

        sort the array - O(nlogn)
        [25, 23, 10, 4]
        only need to consider the first i elements where i = h - len(piles)

        given desired runtime O(nlogm) where m is largest element in array:
            - find the largest element, O(n)
            - start with m / 2. test to see if that succeeds?
            - if it doesn't, binary search. try: (m / 2) + m) / 2
            - if that succeeds, lower and try again
            - each time we test, it's O(n)? how do we test in O(n) time?
                - just iterate through the piles and divide by the test amount,
                  add that to the number of hours. round up
        """
        biggest_pile = max(piles)
        l, r = 0, biggest_pile
        result = biggest_pile

        # not sure what this condition should be yet
        while l <= r:
            mid = l + (r - l) // 2
            if mid == 0:
                break
            # print(f"mid={mid}")
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
                # print(f"hours={hours} for pile={pile}")
                if hours > h:
                    # print(f"hours: {hours}")
                    break

            if hours <= h:
                result = min(result, math.ceil(mid))
                r = mid - 1
            else:
                l = mid + 1

        return result




