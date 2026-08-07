class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        algo:
            - go through board
            - if cell has first letter in word:
                - run bfs or dfs
                - if entire word found: return True
            - return False if we can't find the word

        board=[
            ["A","B","C","E"],
            ["S","F","E","S"],
            ["A","D","E","E"]
        ]
        word="ABCESEEEFS"

        do we need to prevent going backwards?
            - yes

        notes
            - first submission failure: forgot to track visited paths
            - second submission failure: BFS doesn't distinguish between paths,
              so encountering the same letter on multiple paths would mark both
              as seen even if one of them was a valid path and the other wasn't
            - ran into a wall with tracking a global seen set. needed to pass the
              seen set each time in the queue for each unique path.
        """
        start = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == start:
                    k = 0
                    q = [(start, i, j, k, {(i, j)})]
                    while q:
                        curr, x, y, k, seen = q.pop(0)
                        if curr == word:
                            return True
                        if k >= len(word):
                            continue
                        k += 1
                        if (x - 1 >= 0 and board[x - 1][y] == word[k] and (x - 1, y) not in seen):
                            q.append((curr + word[k], x - 1, y, k, seen | {(x - 1, y)}))
                        if (x + 1 < len(board) and board[x + 1][y] == word[k] and (x + 1, y) not in seen):
                            q.append((curr + word[k], x + 1, y, k, seen | {(x + 1, y)}))
                        if (y - 1 >= 0 and board[x][y - 1] == word[k] and (x, y - 1) not in seen):
                            q.append((curr + word[k], x, y - 1, k, seen | {(x, y - 1)}))
                        if (y + 1 < len(board[0]) and board[x][y + 1] == word[k] and (x, y + 1) not in seen):
                            q.append((curr + word[k], x, y + 1, k, seen | {(x, y + 1)}))
        
        return False