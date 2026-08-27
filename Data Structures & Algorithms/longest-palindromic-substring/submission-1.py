class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        brute force:
            iterate over string
                go through entire rest of string
                check if palindrome
                track longest
        
        how can we optimize? what state can we store?

        go through the string
        try moving outwards, keep going until the chars are different

        pseudocode:
            for every char in s:
                pointer for left and right of char
                if left == right, keep going -1 and +1
                if left == char: move left one
                if right == char: move right one
                track longest
            return longest
        """

        res, max_len = "", 0

        for i in range(len(s)):
            l = r = i
            while r < len(s) - 1 and s[r + 1] == s[i]:
                r += 1
            while l >= 1 and r < len(s) - 1:
                if s[l - 1] == s[r + 1]:
                    l -= 1
                    r += 1
                else:
                    break
            if r - l + 1 > max_len:
                res = s[l:r + 1]
                max_len = r - l + 1
            
            # print(f"res: {res}")
            # print(f"max_len: {max_len}")

        return res
