from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        TIME: 7:56.80
        
        valid tree means:
            - can't have cycles
            - can't have any disconnected nodes

        algo:
            - create the adj matrix
            - start from any node, doesn't really matter
            - track seen nodes
            - if cycle, return False
            - if tracked nodes != n, return false
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([0])
        seen = set()
        while queue:
            curr = queue.popleft()
            if curr in seen:
                return False
            
            seen.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in seen:
                    queue.append(neighbor)
            
        return len(seen) == n
