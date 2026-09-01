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
        
        # print(edges)
        
        nodes = set()
        result = 0
        while len(nodes) < len(points):
            cost, point1, point2 = heapq.heappop(edges)
            if point1 in nodes and point2 in nodes:
                continue
            result += cost
            nodes.add(point1)
            nodes.add(point2)

        return result
