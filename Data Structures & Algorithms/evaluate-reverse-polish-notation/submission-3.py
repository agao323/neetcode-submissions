class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        TIME: 13:01.71

        use a stack
            - add to stack until we hit an operator
            - apply operator to numbers in stack
            - push number into stack
            - keep going until we're done
        """
        operators = set(["+", "-", "*", "/"])
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:                
                second = int(stack.pop())
                first = int(stack.pop())
                result = 0

                if t == "+":
                    result = first + second
                if t == "-":
                    result = first - second
                if t == "*":
                    result = first * second
                if t == "/":
                    result = int(first / second)
                
                stack.append(result)
        
        return int(stack[0])