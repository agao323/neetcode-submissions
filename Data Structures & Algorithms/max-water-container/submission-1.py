class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        at every point, we want to find the farthest bar of equivalent height
        or more to give us the maximum amount of water we can store

        brute force:
            - O(n^2), go through all the possible combinations
        
        tricky:
        height = [1,7,8,9,20,7,3,6]
            - even though heights are going up, 7 @ index 1 -> 6 @ index 7
              is still the best, which implies we can't just discard 7 when we see
              8, 9, 20, etc.
            - we can't just scan backwards either, bc that's still O(n^2)
        
        thoughts:
            - maintain a left and right pointer
            - when to move the pointers?
            - start from first and last?
            - check next for each, move over to whichever is bigger
            - keep going until they meet
            - at each point, we always know the bigger height will produce a higher
              potential max
            - [1,7,8,100,1000,7,3,6] doesn't work for this case
            - rather than moving to the next bigger one, move the smaller current height
              because no matter how big the next one is, it will be a smaller value if
              we lower the distance. so move the smaller height in hopes of a bigger
              height later
        """
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            result = max(result, curr)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return result


        """ brute force
    
        res = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                res = max(min(heights[i], heights[j]) * (j - i), res)
        return res
        """
                