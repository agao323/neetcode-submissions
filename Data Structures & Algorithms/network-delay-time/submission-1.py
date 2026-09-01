from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
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
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
    
        # if self.hasCycle(n, times, graph):
        #     return -1
        
        min_dist = {}
        for i in range(n):
            min_dist[i + 1] = 0 if i + 1 == k else math.inf

        visited = set([k])
        queue = [(k, 0)]
        while queue:
            cur, dist = queue.pop(0)
            for neighbor in graph[cur]:
                n, t = neighbor
                new_dist = dist + t
                if n not in visited:
                    queue.append((n, new_dist))
                if new_dist < min_dist[n]:
                    min_dist[n] = new_dist
        
        if any([d == math.inf for d in min_dist.values()]):
            return -1
        return max(min_dist.values())


    # def hasCycle(self, n, times, graph) -> bool:
    #     indegs = {i: 0 for i in range(1, n + 1)}
    #     for u, v, _ in times:
    #         indegs[v] += 1
        
    #     queue = [k for k, v in indegs.items() if v == 0]
    #     while queue:
    #         cur = queue.pop(0)
    #         for neighbor in graph[cur]:
    #             n, t = neighbor
    #             indegs[n] -= 1
    #             if indegs[n] == 0:
    #                 queue.append(n)
        
    #     return any([v != 0 for k, v in indegs.items()])








