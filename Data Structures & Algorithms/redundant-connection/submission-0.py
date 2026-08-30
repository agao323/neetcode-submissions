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
        
        question is: can we remove ANY edge from the cycle? I think yes
        """
        indegrees = [0] * (len(edges) + 1)
        for u, v in edges:
            indegrees[u] += 1
            indegrees[v] += 1
        
        cycle_nodes = set([i for i in range(1, len(indegrees)) if indegrees[i] > 1])

        for e1, e2 in edges[::-1]:
            if e1 in cycle_nodes and e2 in cycle_nodes:
                return [e1, e2]
        
        return []