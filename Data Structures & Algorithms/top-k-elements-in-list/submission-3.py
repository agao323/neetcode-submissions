from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        TIME: 17:38.97
            - note: time to complete initial thoughts. did not do optimized
        TIME: 29:56.55
            - includes initial time + time to complete optimized bucket strategy

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

        optimized solution is bucket sorting (looked at solution)
        time: O(n). building counts is O(n), creating bucket O(n), iterating bucket O(n) so O(3n)
        space: O(n). also O(3n) for dict, bucket and res
        """

        # bucket sort
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        # question assumes answer is always unique
        # duplicate frequencies ARE possible, they'll just always be included?
        # initialize to empty list since nums[i] can be negative
        # but it really just represents undefined
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in counts.items():
            bucket[val].append(key)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if len(bucket[i]) > 0:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        return res


        # ACCEPTED O(nlogk) solution below

        # counts = defaultdict(int)
        # for num in nums:
        #     counts[num] += 1
        
        # heap = [(-v, k) for k, v in counts.items()]
        # heapq.heapify(heap)

        # result = []
        # for _ in range(k):
        #     result.append(heapq.heappop(heap)[1])
        # return result
