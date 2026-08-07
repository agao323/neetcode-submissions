class MinStack:
    """
    TIME:
        17:56.07

    solution:
        - just create a class that tracks the min at each element
            - don't even need stack, just use tuple
        - push
            - push to stack
            - min = min(val, top.val)
        - pop
            - normal pop
        - top
            - normal top
        - getMin
            - top.min
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            top_val, top_min = self.stack[-1]
            curr_min = min(val, top_min)
            self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
