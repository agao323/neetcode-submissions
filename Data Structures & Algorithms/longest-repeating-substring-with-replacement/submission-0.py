from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        thoughts:
            - minimum length is always k
            - generally, find the longest substring first
            - minimum answer is longest substring + k
            - now how do we figure out bridges where k can fill the gap?
            - find the longest substring without replacements
            - look to the left and right, using k replacements
            - keep going until we're out of k and encounter a different letter

        ^ this doesn't account for something like ABABA, or AABBAABBAA
        where we have multiple longest substrings to account for

        sliding window solution?
        at any point, we can only have two unique characters
        the max occurrence of the less frequently occuring char has to be <= k
        
        example: ABBBACBAABAA, k = 2
                 BBBAACAAAABA, k = 2, answer: 9
            - as soon as we see C, we know it's no longer a valid window
            - actually, C being a different character doesn't matter
                - what matters is that less frequent char is now > k
            - we can't discard everything either
            - track number of duplicates in each window?
            - once sum(non duplicates) - k > 0, move left forward until it's 0
            - in example below, B: 2, A: 2, C: 1 is still invalid
                - B: 1, A: 2, C: 1 is valid though
            - keeps going until {B: 2, A: 6, C: 1}
                - then: {B: 1, A: 6, C: 1} is now valid
                - finally: {B: 1, A: 7, C: 1} is the final result
                - gives us our answer of 9
            {
                B: 3
                A: 2
                C: 1
            }
        """
        if not s:
            return 0

        letters = defaultdict(int)
        l, r = 0, 0
        result = 0
        max_char = s[0]
        other_count = 0

        while r < len(s):
            # print(letters)
            letters[s[r]] += 1

            # if it's the current max, we're fine, just add one
            if s[r] == max_char:
                # print(f"sum of letter values: {sum(letters.values())}")
                result = max(result, sum(letters.values()))
            
            # otherwise - check if sum(others) > k
            else:
                other_sum = sum(letters.values()) - letters[max_char]

                # start moving left pointer over
                if other_sum > k:
                    while other_sum > k:
                        letters[s[l]] -= 1
                        l += 1
                        other_sum -= 1
                
                if letters[s[r]] > letters[max_char]:
                    max_char = s[r]
            
            r += 1
        
        return max(result, sum(letters.values()))













