import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = [-1 * num for num in nums][::-1]
        self.k = k
        
    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -1 * val)
        
        temp = []
        for _ in range(self.k):
            temp.append(heapq.heappop(self.max_heap))
        
        ret = -1 * temp[-1]
        for val in temp:
            heapq.heappush(self.max_heap, val)
            
        return ret
