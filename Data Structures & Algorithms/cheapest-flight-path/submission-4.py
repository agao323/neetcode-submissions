from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        build the graph and include the prices next to each destination

        use a min heap to track the node, the current price, and the current # of stops
        formatted this way: (price, airport, stops)

        do a bfs:
            get the top of the heap
            check if we're at destination. if yes, return the price
            check all neighbors
                if stops + 1 > k, ignore
                otherwise, push (cur price + neighbor price, neighbor airport, stops + 1)
        
        return -1

        time complexity: O(E + Vlog(V))

        """
        INF = 1e10
        prices = [INF] * n
        prices[src] = 0

        for i in range(k + 1):
            new_prices = list(prices)
            for _src, _dst, cost in flights:
                if prices[_src] == INF:
                    continue
                new_prices[_dst] = min(new_prices[_dst], prices[_src] + cost)
                # print(f"src/dst/cost: {_src, _dst, cost} prices: {new_prices}")
            prices = new_prices
        
        return prices[dst] if prices[dst] != INF else -1



        """
        graph = defaultdict(list)
        for from_i, to_i, price_i in flights:
            graph[from_i].append((to_i, price_i))
        

        min_heap = [(0, src, 0)]

        while min_heap:
            cur_price, airport, stops = heapq.heappop(min_heap)
            if airport == dst:
                return cur_price
            
            for airport, price in graph[airport]:
                if stops > k:
                    continue
                heapq.heappush(min_heap, (cur_price + price, airport, stops + 1))
        
        return -1
        """
