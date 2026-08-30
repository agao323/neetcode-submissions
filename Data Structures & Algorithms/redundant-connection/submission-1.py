from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        naive: go through all edges, remove them, check if graph is connected
               and non-cyclical. O(E * (V + E)) time complexity
        
        we can leverage an insight here maybe:
            - the edge to be removed MUST be between nodes with 2+ edges. if
              a node only has a single edge, it can't be part of a cycle
            - the cycle must be 3+ nodes, because it's undirected, so just
              two nodes can't form a cycle between themselves

        alternatively:
            - the edge to be removed MUST be part a cycle, and a cycle is
              by definition guaranteed to exist. this means we can use kahn's
              algorithm to narrow down which nodes are part of the cycle,
              and then go through the edges to find the first edge that 
              connects two nodes in this set of cyclical nodes.
                time: O(V + E) + O(E), so just O(V + E)
            - correction: cant use kahn's algo, think that's just for
              directed graphs
        
        question is: can we remove ANY edge from the cycle? I think yes
        this is actually just a cycle detection problem. figure out what
        nodes are involved in the cycle and remove any edge, and we're good

        track a prev node somehow? so we know which node we came from?
        then if we see a node we've visited but isn't the node we came from,
        we know it's a cycle. just exclude the parent when detecting cycles
        """
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        cycle = set()
        def dfs(node, path, parent):
            nonlocal cycle
            if node in visited:
                i = path.index(node)
                if len(set(path[i:])) > len(cycle):
                    cycle = set(path[i:])
                # print(cycle)
                return
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, path + [nei], node)  
        
        dfs(1, [1], -1)
        # print(cycle)

        for e1, e2 in edges[::-1]:
            if e1 in cycle and e2 in cycle:
                return [e1, e2]
        
        return []







