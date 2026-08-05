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
        intervals.sort(key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            first = intervals[i - 1]
            second = intervals[i]

            if first.start < second.end:
                return False
        
        return True