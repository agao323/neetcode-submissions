class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        TIME: 
            39:37 - gave up and looked at solution
            50:56.32 - implemented greedy O(n) time O(1) space solution
        
        notes:
            - definitely need to come back to this one and learn the 2d dp solution
            - fully just copied solution here, not sure if I even fully understand

        brute force:
            - every * can be '(', '', or ')'
            - generate every possibility and check if valid
            - O(3^n) if every char is *, ie "***" gives 27 combinations to check

        stack + backtracking?
            - open parens '(' -> push onto stack
            - close parens ')' -> try to pop and open parens from stack
            - asterisk: explore all three options

        any better optimizations? probably dp
        """
        
        left_min, left_max = 0, 0

        for c in s:
            if c == '(':
                left_min += 1
                left_max += 1
            elif c == ')':
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0
