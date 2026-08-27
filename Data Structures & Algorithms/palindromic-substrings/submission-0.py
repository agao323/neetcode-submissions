class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Can apply the O(n^2) solution here where we expand outwards
        any time we see a valid palindrome, count it

        algo:
            track num of substrings in result
            iterate through each char in s
                separate tracking for odd and even
                expand outwards and increment if s[l] == s[r]
            return result
        """

        result = 0

        for i in range(len(s)):
            # odd
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            
        return result
