class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    
    def find(self, node) -> int:
        while self.parents[node] != node:
            node = self.parents[node]
        return node
    
    def union(self, u, v) -> bool:
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        pu_size = self.size[pu]
        pv_size = self.size[pv]
        if pv_size > pu_size:
            pu, pv = pv, pu
        
        self.size[pu] += self.size[pv]
        self.parents[pv] = self.parents[pu]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        TIME:
            1:08:09 - had to brush up on MST algorithms, ie prims/kruskals

        naive: O(n^2), go through and find the closest point, connect
                to the closest point 
        """
        edges = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                edges.append((dist, i, j))

        edges.sort()
        dsu = DSU(len(points))
        result = 0
        for dist, p1, p2 in edges:
            if dsu.union(p1, p2):
                result += dist
        
        return result


        """
        if len(points) == 1:
            return 0

        graph = collections.defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                graph[(x1, y1)].append(((x2, y2), weight))
                graph[(x2, y2)].append(((x1, y1), weight))
        
        # initialize mst with arbitrary first point
        min_heap = [(0, (points[0][0], points[0][1]))]
        total_weight = 0
        visited = set()

        # iterate until we add all vertices and have an MST
        while len(visited) < len(points):
            # print(min_heap)
            # print(total_weight)
            weight, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_weight += weight

            for neighbor in graph[node]:
                n, w = neighbor
                if n not in visited:
                    heapq.heappush(min_heap, (w, n))

        return total_weight
        """
