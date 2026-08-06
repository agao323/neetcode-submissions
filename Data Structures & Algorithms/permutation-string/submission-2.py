from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        TIME: 17:49.89
            - implementation is still wonky
            - missed edge cases caught by submitting:
                - s1 empty, s2 empty, len(s1) > len(s2)
            - still need to figure out how to handle end of list cases, ie:
                s1 = "ee" and s2 = "abcdee" 
                matches at the end, right now I keep having to handle outside the loop

        initial thoughts:
            - maintain a sliding window of size len(s1)
            - compare equivalency in dicts:
                1. char counts for s1
                2. char counts for current window
        """
        if not s1: 
            return True

        if not s2 or len(s1) > len(s2):
            return False

        s1_counts = defaultdict(int)
        for c1 in s1:
            s1_counts[c1] += 1
        
        s2_counts = defaultdict(int)
        for i in range(len(s1)):
            s2_counts[s2[i]] += 1
        
        l, r = 0, len(s1)
        while r < len(s2):
            if s1_counts == s2_counts:
                return True
            
            s2_counts[s2[l]] -= 1
            if s2_counts[s2[l]] == 0:
                del s2_counts[s2[l]]
            l += 1
            s2_counts[s2[r]] += 1
            r += 1
        
        return s1_counts == s2_counts