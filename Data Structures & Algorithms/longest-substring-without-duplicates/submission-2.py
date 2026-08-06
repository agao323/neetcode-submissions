from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        TIME: 12:16.65
            - lots of small gotchas here that tripped me up:
                need to make sure the new start is greater than the old one
                need to check the end as an edge case
                need to make sure starting 1 over
                
        zxyzxyz
        zxyxzxyz

        thoughts:
            - track the starting point of the current substring
            - track the current max
            - dict of letter to index where that letter most recently appeared
            - chop off anything after the index where letter most recently was
            - continue moving forward and return the max
        """
        start, longest = 0, 0
        letters_to_index = defaultdict(int)

        for i in range(len(s)):
            c = s[i]
            if c in letters_to_index:
                # need to start chopping
                longest = max(longest, i - start)
                if letters_to_index[c] + 1 > start:
                    start = letters_to_index[c] + 1
                letters_to_index[c] = i
            letters_to_index[c] = i
        
        return max(longest, len(s) - start)

