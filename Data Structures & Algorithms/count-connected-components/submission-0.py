from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        thoughts:
            - build the adjacency matrix to represent the graph
            - algorithm:
                - maintain a set of seen nodes
                - go through every node and traverse the CC
                - add all the nodes to the seen set
                - add 1 every time we finish going through every CC
                - return result
        """
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
            
            q = [i]
            while q:
                curr = q.pop(0)
                seen.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        q.append(neighbor)

            count += 1
        
        return count
