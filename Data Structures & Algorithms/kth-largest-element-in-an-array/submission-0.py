class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        maintain a min heap of size k, so the first element
        is always the kth largest of what we've currently scanned

        if we encounter an element larger than the top of the heap,
        we insert it and pop until it's size k still
        
        return top of heap for O(nlogk) > O(nlogn)
        """
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num < min_heap[0]:
                continue
            else:
                heapq.heappush(min_heap, num)
                while len(min_heap) > k:
                    heapq.heappop(min_heap)
        
        return min_heap[0]