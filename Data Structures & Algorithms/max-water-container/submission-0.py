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
        
        """
        res = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                res = max(min(heights[i], heights[j]) * (j - i), res)
        return res
                