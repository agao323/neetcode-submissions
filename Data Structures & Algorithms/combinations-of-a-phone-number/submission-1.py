class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        TIME: 20:56.32
            - took me way to long to remember how to handle the nuances here
            - need to learn the backtracking approach
        """
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