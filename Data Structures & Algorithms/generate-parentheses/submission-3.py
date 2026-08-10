from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        TIME: 
            9:01.11 - BFS


        brute force:
            - generate all possible combos
            - check validity on each one
            - O(2^n * n)
        
        BFS:    
            - always starts with (
            - at every point, track open and closed counts. open
              starts at n - 1
            - as long as open > 0 and closed > 0
            - we can add curr + open, curr + closed to the queue
            - append result to queue when open == closed == 0
        """

        """ DFS
        """
        result = []

        def dfs(curr: str, open: int, closed: int) -> None:
            if open == 0 and closed == 1:
                result.append(curr + ')')
                return
            
            if open > 0:
                dfs(curr + '(', open - 1, closed)
            if closed > 0 and closed > open:
                dfs(curr + ')', open, closed - 1)
        
        dfs('(', n - 1, n)
        return result


        """ BFS

        if n == 0:
            return []

        result = []
        queue = deque([('(', n - 1, n)])
        while queue:
            curr, open, closed = queue.popleft()
            # we only have one option left: closed parens
            if open == 0 and closed == 1:
                result.append(curr + ')')
                continue
            if open > 0:
                queue.append((curr + '(', open - 1, closed))
            # extra check here: can't add a closed without an open
            if closed > 0 and closed > open:
                queue.append((curr + ')', open, closed - 1))

        return result
        """