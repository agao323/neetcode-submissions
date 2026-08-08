from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        TIME: 
            7:13.97
                - runtime is really bad (beats 0.96%), looking into optimizations
            29:20.74 - TOTAL for BFS + DFS + UNION FIND

        thoughts:
            - build the adjacency matrix to represent the graph
            - algorithm:
                - maintain a set of seen nodes
                - go through every node and traverse the CC
                - add all the nodes to the seen set
                - add 1 every time we finish going through every CC
                - return result
        """

        """ UNION FIND TIME: 19:36.84
            - ran into some issues with the code

        algo:
            - two arrs
                1. parent tracker
                2. rank tracker
            
            - track a result which starts at n, in which case every
              node is an isolated component. decrement by one every
              time we do a successful union
            
            - union:
                find parents of both
                use parent with higher rank. if same, doesn't matter
                assign parent to be the same root (path compression)
                every successful union decrements result by one
                    unsuccessful union means they were already in the
                    same component

            - find:
                get the parent pointer in the parent arr
        """
        parents = [i for i in range(n)]
        ranks = [1] * n
        
        def find(node) -> int:
            # gives us the parent node
            while parents[node] != node:
                # path compression
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node
        
        def union(one, two) -> bool:
            # returns bool to tell us if successful or not
            one_parent = find(one)
            two_parent = find(two)
            if one_parent == two_parent:
                # already in the same component
                return False

            one_rank = ranks[one_parent]
            two_rank = ranks[two_parent]

            if one_rank >= two_rank:
                parents[two_parent] = one_parent
                ranks[one_parent] += 1
            else:
                parents[one_parent] = two_parent
                ranks[two_parent] += 1

            return True


        result = n
        for u, v in edges:
            if union(u, v):
                result -= 1
        
        return 1 if result < 1 else result





        """ DFS TIME: 2:29.93

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
        """

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
