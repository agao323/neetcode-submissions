class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        naive: O(n^2), go through and find the closest point, connect
                to the closest point 
        """
        if len(points) == 1:
            return 0

        graph = collections.defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, points):
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

