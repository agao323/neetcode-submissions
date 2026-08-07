class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        brute force:
            - O(n^2), search whole array for every element to find a warmer temp
        
        thoughts:
            - use a stack maybe?
            - if we find a bigger number, pop from the stack
            - if we don't, add to the stack
            - when we pop, if there's a number inside, add to its count
            - keep popping from the stack as long as the current number
              is larger than the top of the stack

        algo:
            - initialize result array to all 0s
            - insert the first element to the stack with value 0
            - if temp[i] > stack.top(), pop from stack and assign
              stack.top() in result array. track the index too:
                (temp, index, val)
            - if temp[i] <= stack.top():
                add to stack: (temp, i, 0)
            - number of times we had to pop is really what the value should be

            [1,4,1,2,1,0,0]

            [(40, 5), (28, 6)]
        """
        if len(temperatures) < 2:
            return temperatures

        result = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            if temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    top_temp, top_i = stack.pop()
                    result[top_i] = i - top_i
                stack.append((temperatures[i], i))
        
        return result









    