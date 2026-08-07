class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        algo: greedy + two pointers?
            - two pointers? left and right
            - keep advancing right until we find a word
            - mark that index as valid
            - advance left to right
            - if both pointers end up at the last index, we're good?
            - what if we work backwards.. shouldn't be different?
        
        second approach:
            - create a separate array with valid indices
            - if the array holds a 1, that's a valid place to start/end a word
            - intialize index 0 with a 1
            - if we ever find the last index to be 1, we're done
            - move l up to the next index 1 each time instead of l = r
        """
        if not s or not wordDict:
            return False
        if len(s) == 1:
            return s in wordDict

        l, r = 0, 1
        words = set(wordDict)
        breaks = [0] * (len(s) + 1)
        breaks[0] = 1

        while l < r and r <= len(s):
            print(f"s[l:r]: {s[l:r]}")
            if s[l:r] in words:
                breaks[r - 1] = 1
            
            r += 1
            if r > len(s):
                # ran out of letters, move to next break
                l += 1
                while l < r and breaks[l] != 1:
                    l += 1
                # start at next letter
                l += 1
                r = l + 1
        
        print(f"l, r = {l}, {r}")
        print(f"breaks: {breaks}")
        return breaks[-2] == 1
