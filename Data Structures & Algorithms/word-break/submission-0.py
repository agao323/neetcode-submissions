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
        """

        l, r = 0, 0
        words = set(wordDict)

        while r <= len(s):
            if s[l:r] in words:
                l = r
            r += 1
        
        l += 1
        return l == r
