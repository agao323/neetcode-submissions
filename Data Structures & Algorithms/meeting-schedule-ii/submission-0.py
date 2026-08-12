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

        result = 1
        intervals.sort(key=lambda i: i.end)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                result += 1
            elif result > 1:
                result -= 1
        
        return result

        