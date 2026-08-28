import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        TIME:
            11:49 - caught up a bit on the minheap stuff, should have been faster

        maintain a min heap of size k so we get O(nlogk) time
        don't need sqrt, (x1 - x2) ** 2 + (y1 - y2) ** 2 is monotonically increasing
        """

        heap = []

        for p in points:
            x, y = p[0], p[1]
            dist = -(x ** 2 + y ** 2)

            if heap and dist <= heap[0][0] and len(heap) == k:
                continue
            
            heapq.heappush(heap, (dist, x, y))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [[x, y] for (_, x, y) in heap] 
