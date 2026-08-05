from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        two parts to this problem:
        1. figure out if a word already has an anagram
        2. group them together in a dict

        how do we know if an anagram exists? how to uniquely identify one?
        - serialize each word. char + count in alphabetical order
        - ie: act -> a1c1t1, cat gives the same -> a1c1t1

        utilize efficient method of counting using ord() and 26 len array
        dict looks like:
        {
            "a1c1t1" -> ["act", "cat"]
            ...
        }

        then just output the values in the dict

        time: O(n * m) where n = len(strs) and m = len of each str
        space: O(n * m)
        """
        groups = defaultdict(list)
        for s in strs:
            key = self.serialize(s)
            groups[key].append(s)
        
        return [v for k,v in groups.items()]
    
    def serialize(self, word: str) -> str:
        counts = [0] * 26
        for c in word:
            counts[ord(c) - ord('a')] += 1
        
        output = ""
        for i in range(len(counts)):
            if counts[i] == 0:
                continue
            char = chr(ord('a') + i)
            output += f"{char}{counts[i]}"
        
        return output
