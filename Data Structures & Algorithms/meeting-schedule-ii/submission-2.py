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
        calculate max overlaps

        sort by end time
        [(5,10),(15,20),(10,40),(50,60)]
            curr.start < prev.end -> need another room
        """
        if len(intervals) <= 1:
            return len(intervals)

        result, rooms = 1, 1
        intervals.sort(key=lambda i: i.end)

        # print([(i.start, i.end) for i in intervals])

        curr = intervals[0]
        curr_end = intervals[0].start
        for interval in intervals[1:]:
            if interval.start < curr_end:
                rooms += 1
                result = max(result, rooms)
            else:
                curr = interval
                curr_end = interval.end
                rooms = 1
        
        return result

        