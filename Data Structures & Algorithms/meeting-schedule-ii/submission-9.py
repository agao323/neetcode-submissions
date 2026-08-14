"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        TIME: 15:44.18
            this was after reading the solution and then trying again
            the next day after digesting and understanding it

        calculate max overlaps

        [(1,2),(3,5),(4,6)]
        [1,3,4,100]
        [5,6,7,101]

        1. separate the start and end times
        2. sort each one
        3. go through the starts
            - increment room count by 1 until a start > curr_end
                - basically, the first meeting has ended so a room is free
                - as long as there are meetings starting when the globally
                  first meeting to end hasn't ended, we need more rooms
                - when we increment the end time, decrement rooms needed
                  by one since a room is freed
            - track the global maximum
            - keep going until we're out of starts
                - don't care about when the meetings end, we only need
                  new rooms for meetings that are going to start
        """

        """ heap solution

        store end times, top is the earliest ending meeting
        """
        import heapq
        
        intervals.sort(key=lambda i: i.start)
        end_heap = []
        for i in intervals:
            # earliest end time completes before current start
            # so we can free up a room
            if end_heap and end_heap[0] <= i.start:
                heapq.heappop(end_heap)
            # we freed up a room but there's a new meeting, so we
            # still have to occupy a room for the current meeting
            heapq.heappush(end_heap, i.end)
            
        return len(end_heap)


        """ two pointer solution

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        s, e = 0, 0
        total, curr = 0, 0
        while s < len(starts):
            start, end = starts[s], ends[e]
            if start < end:
                curr += 1
                total = max(total, curr)
                s += 1
            else:
                # room freed up
                curr -= 1
                e += 1
        
        return total

        """


