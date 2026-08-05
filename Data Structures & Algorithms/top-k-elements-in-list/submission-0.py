from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        initial thoughts:
        1. count occurrence of each element in dict
        2. throw into heap
        3. pop k times

        optimized?
        use a heap + dict at the same time
        heap tracks current top k
        dict tracks occurrences
        what happens when the order changes? then we have to pop and push back into heap
            - worst case could still be O(nlogn)
        """

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        heap = [(-v, k) for k, v in counts.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
