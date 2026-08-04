import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # keep a max heap, take the top two elements
        # run the stone smashing logic
        # repeat until there's <= 1 elements left in the heap

        max_heap = [-1 * stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            diff = abs(stone1 - stone2)

            if diff > 0:
                heapq.heappush(max_heap, -1 * diff)
        
        return -1 * max_heap[0] if max_heap else 0
