from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        TIME: 7:13.97
            - runtime is really bad (beats 0.96%), looking into optimizations

        thoughts:
            - build the adjacency matrix to represent the graph
            - algorithm:
                - maintain a set of seen nodes
                - go through every node and traverse the CC
                - add all the nodes to the seen set
                - add 1 every time we finish going through every CC
                - return result
        """

        """ DFS TIME: 2:29.93
        """
        graph = defaultdict(list)
        for a, b in edges:
            # add both since it's undirected, although probably not necessary?
            graph[a].append(b)
            graph[b].append(a)

        visited, count = set(), 0

        def dfs(node: int) -> None:
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            count += 1
        
        return count

        """ BFS TIME 7:13.97

        graph = defaultdict(list)
        for a, b in edges:
            # add both since it's undirected, although probably not necessary?
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        count = 0
        for i in range(n):
            # traverse the CC
            if i in seen:
                continue
            
            q = deque([i])
            while q:
                curr = q.popleft()
                seen.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        q.append(neighbor)

            count += 1
        
        return count
        """
