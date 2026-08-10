from collections import defaultdict

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
            TIME: 14:33.16
        """
        if not node:
            return None

        graph = defaultdict(list)

        # BFS through the graph and build the adj matrix
        queue = deque([node])
        seen = set()
        while queue:
            curr = queue.popleft()
            seen.add(curr.val)
            graph[curr.val] = [neigh.val for neigh in curr.neighbors]
            for n in curr.neighbors:
                if n.val not in seen:
                    queue.append(n)

        # create the new references for each node
        val_to_node = {
            val: Node(val) for val in graph.keys()
        }

        # assign the neighbors using the adj matrix and the new references
        for val, node in val_to_node.items():
            node.neighbors = [
                val_to_node[n] for n in graph[val]
            ]

        return val_to_node.get(1)




        