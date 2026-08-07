class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        algo:
            - go through board
            - if cell has first letter in word:
                - run bfs or dfs
                - if entire word found: return True
            - return False if we can't find the word

        what if we have a board like:
        ["A","A","A"]
        ["A","A","A"]
        ["A","A","A"]

        do we need to prevent going backwards?
            - don't think so, since it won't get triggered for words anyways
        """
        start = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == start:
                    k = 0
                    seen = set()
                    q = [(start, i, j, k)]
                    while q:
                        curr, x, y, k = q.pop(0)
                        if (x, y) in seen:
                            continue
                        seen.add((x, y))
                        if curr == word:
                            return True
                        if k >= len(word):
                            continue
                        k += 1
                        if (x - 1 >= 0 and board[x - 1][y] == word[k]):
                            q.append((curr + word[k], x - 1, y, k))
                        if (x + 1 < len(board) and board[x + 1][y] == word[k]):
                            q.append((curr + word[k], x + 1, y, k))
                        if (y - 1 >= 0 and board[x][y - 1] == word[k]):
                            q.append((curr + word[k], x, y - 1, k))
                        if (y + 1 < len(board[0]) and board[x][y + 1] == word[k]):
                            q.append((curr + word[k], x, y + 1, k))
        
        return False