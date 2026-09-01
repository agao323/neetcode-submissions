from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        TIME:
            47:21 - interesting twist on graph problems where we need to
                    essentially check every edge and cycles are allowed

        Seems like classic djikstra's

        Top sort + priority queue, figure out how long until we visit all nodes
        or if there's a cycle or we can't visit all nodes, return -1

        How do we track the minimum time for all nodes? Typically djikstra is
        shortest weighted path from node 1 -> node 2

        We can maintain a separate dict that stores the minimum distance to
        each node from the starting node k, and just return the max in that dict

        algo:
            build the graph u -> [(v1,t1), (v2,t2), ...]

            detect cycles first with kahn's and return early if we find
            any. don't need to consider the cost for cycle detection

            initialize:
                queue - for bfs through the graph. don't need heap
                    initialize with (k, 0)
                min_dist - dict for minimum distances for each node
            traverse the graph:
                pop first element in queue
                for each neighbor n of current:
                    add (n, dist) to the queue
                    if dist less than curr min for n:
                        update min_dist
            
            if any min_dist is -1, we couldn't reach that node
            otherwise return the max value in min_dist
        """

        """ SPFA (shortest path faster algorithm)

        optimized bellman-ford. use a queue to optimize the nodes
        that get considered, and skip any that are not shorter paths.
        only add nodes to the queue if we do find a shorter path and
        there's potentially a shorter path to another node through that
        node that we just processed.

        maintain separate dict that tracks shortest path to each node,
        and return the max of that as long as it's < inf
        """

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i: math.inf for i in range(1, n + 1)}
        dist[k] = 0

        queue = deque([(k, 0)])
        while queue:
            node, time = queue.popleft()
            if dist[node] < time:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    queue.append((neighbor, new_time))
        
        result = max(dist.values())
        return result if result != math.inf else -1


        """ djikstra: O(ElogV)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        result = 0
        while min_heap:
            dist, cur = heapq.heappop(min_heap)
            if cur in visited:
                continue
            visited.add(cur)
            result = dist

            for node, weight in graph[cur]:
                if node not in visited:
                    heapq.heappush(min_heap, (dist + weight, node))

        return result if len(visited) == n else -1
        """


        """ bellman-ford

        dist = [math.inf] * (n + 1)
        dist[k], dist[0] = 0, -1

        for _ in range(n - 1):
            for u, v, w in times:
                dist[v] = min(dist[v], dist[u] + w)
        
        max_dist = max(dist)
        return -1 if max_dist == math.inf else max_dist
        """


        """ my initial hacky ass approach

        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        min_dist = {}
        for i in range(n):
            min_dist[i + 1] = 0 if i + 1 == k else math.inf

        visited_edges = set()
        queue = [(0, k)]
        heapq.heapify(queue)
        while queue:
            dist, cur = heapq.heappop(queue)
            for neighbor in graph[cur]:
                n, t = neighbor
                new_dist = dist + t
                if (cur, n, t) not in visited_edges:
                    heapq.heappush(queue, (new_dist, n))
                    visited_edges.add((cur, n, t))
                    if new_dist < min_dist[n]:
                        min_dist[n] = new_dist
            if len(visited_edges) == len(times):
                break

        if any([d == math.inf for d in min_dist.values()]):
            return -1
        return max(min_dist.values())
        """







