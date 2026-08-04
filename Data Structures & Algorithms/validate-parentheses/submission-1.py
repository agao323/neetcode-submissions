class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {
            ')': '(',
            '}': '{', 
            ']': '['
        }

        stack = []
        open_parens = ['(', '{', '[']
        close_parens = [')', '}', ']']

        for c in s:
            if c in open_parens:
                stack.append(c)
            elif c in close_parens:
                if stack:
                    top = stack.pop()
                    if valid_pairs[c] != top:
                        return False
                else:
                    return False
        
        return len(stack) == 0
