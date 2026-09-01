class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        naive: O(n^2), go through and find the closest point, connect
                to the closest point 
        """
        if len(points) == 1:
            return 0

        seen = set()
        edges = []
        for x in points:
            for y in points:
                if x == y:
                    continue
                x_t, y_t = (x[0], x[1]), (y[0], y[1])
                weight = abs(x_t[0] - y_t[0]) + abs(x_t[1] - y_t[1])
                if (weight, x_t, y_t) in seen or (weight, y_t, x_t) in seen:
                    continue
                heapq.heappush(edges, (weight, x_t, y_t))
                seen.add((weight, x_t, y_t))
        
        graph = collections.defaultdict(list)
        for w, p1, p2 in edges:
            graph[p1].append((p2, w))
            graph[p2].append((p1, w))

        # initialize mst with arbitrary first point
        min_heap = [(0, (points[0][0], points[0][1]))]
        total_weight = 0
        visited = set()

        # iterate until we add all vertices and have an MST
        while min_heap:
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

