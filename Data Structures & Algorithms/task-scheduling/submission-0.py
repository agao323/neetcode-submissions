from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        greedy algo with heap + queue
            cooldown queue:
                - when we pop from heap, we add to a queue
                - store (task, count, next available cycle)

            so algo becomes:
                - build a heap with the counts
                - get the first task from the heap and run it. if
                  more tasks remain, add to cooldown queue
                - we always know the front of the queue is
                  a task available for processing as long as
                  curr cycle >= next available cycle, so add it
                  back into the heap. we don't necessarily process
                  the first element in the queue if there are
                  higher count tasks in the heap
                - if front of queue is not available and the heap
                  is empty, then we idle
                - when a task reaches 0 remaining count, we're done
                  and don't add back to queue
                - keep going until both heap and queue is empty
        """        
        counts = Counter(tasks)

        heap = []
        for task, count in counts.items():
            heapq.heappush(heap, (-count, task))

        cooldown = deque([])

        cycle = 0
        while heap or cooldown:
            # keep checking front of cooldown queue to see
            # if it's ready, ie whether current cycle is greater
            # than or equal to the next available cycle we assigned
            while cooldown:
                first = cooldown[0]
                next_available_cycle = first[2]
                if cycle >= next_available_cycle:
                    first = cooldown.popleft()
                    heapq.heappush(heap, (first[1], first[0]))
                else:
                    break

            # anything in the heap is available for processing,
            # so process and add to the cooldown queue
            if heap:
                top = heapq.heappop(heap)
                count, task = top[0], top[1]
                next_cycle = cycle + n + 1
                if count + 1 < 0:
                    cooldown.append((task, count + 1, next_cycle))
            
            # increment the cycle, even if nothing from the heap
            # is processed. this simulates an idle cycle
            cycle += 1

        return cycle
        
