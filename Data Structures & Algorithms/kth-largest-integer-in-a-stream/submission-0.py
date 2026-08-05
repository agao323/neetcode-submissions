import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = []
        self.k = k
        
    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)

        if not self.max_heap:
            return -1
        if self.k - 1 > len(self.max_heap):
            return self.max_heap[-1]
        
        print(self.max_heap)
        print(self.k - 1)
        return self.max_heap[self.k - 1]
