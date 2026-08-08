class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []

        queue = [""]
        while queue:
            curr = queue.pop(0)
            if len(curr) == len(digits):
                result.append(curr)
                continue
            d = digits[len(curr)]
            for c in letters[int(d)]:
                queue.append(curr + c)
        
        return result