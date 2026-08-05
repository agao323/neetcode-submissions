import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        # heapify doesn't return anything
        # heapq is always a MIN heap
        heapq.heapify(nums)
        self.k = k

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        
    def add(self, val: int) -> int:
        if val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]
