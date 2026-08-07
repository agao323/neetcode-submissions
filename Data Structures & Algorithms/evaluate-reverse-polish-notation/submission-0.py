class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
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
                # edge case probably not checked in this question
                # shouldn't return -1 but oh well
                if len(stack) != 2:
                    return -1
                
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
        
        return stack[0]
