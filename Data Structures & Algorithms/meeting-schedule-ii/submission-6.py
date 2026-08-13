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

        if len(intervals) <= 1:
            return len(intervals)

        end_heap = [intervals[0].end]
        result, curr = 1, 1
        for i in intervals[1:]:
            if end_heap and i.start >= end_heap[0]:
                heapq.heappop(end_heap)
                curr -= 1
            else:
                heapq.heappush(end_heap, i.end)
                curr += 1
                result = max(result, curr)
            
        return result


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


