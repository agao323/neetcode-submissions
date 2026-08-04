"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Greedy algo?
        - sort by start time
        - sort by end time
        - does it matter?
        """

        intervals = sorted(intervals, key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            prev_start, prev_end = intervals[i-1].start, intervals[i-1].end

            if start < prev_end:
                return False
        
        return True