from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        letters = [0] * 26
        
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1

        for l in letters:
            if l != 0:
                return False
        
        return True
