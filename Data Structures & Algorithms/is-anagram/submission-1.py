from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1

        print(s_dict)
        
        t_dict = defaultdict(int)
        for c in t:
            t_dict[c] += 1

        for k, v in s_dict.items():
            if k not in t_dict:
                return False
            if v != t_dict[k]:
                return False
        
        for k, v in t_dict.items():
            if k not in s_dict:
                return False
            if v != s_dict[k]:
                return False

        return True