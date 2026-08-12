class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        TIME:
            18:05.59
                solution somewhat works, just unable to account for intervals
                that start and stop on same number. going back to sorting

            27:35.75
                completed regular sorting solution

        sort and merge would be straightforward
        what about an array with starts and stops marked?
            starts always override a stop in a slot
            stops do not override a start
            scan the final array for start -> stop intervals

            [[1,3],[1,5],[4,5]
            [0, 2, 0, -1, 1, -2] -> [1,3],[4,5] so that wouldn't work
            could keep scanning until we hit 0? then we know to skip
            the middle ones
            [1,2],[2,3] would give us [0,1,0,-1] since the 2s cancel out
        """

        max_num = max([i[0] for i in intervals])
        ends = [0] * (max_num + 1)

        for start, end in intervals:
            ends[start] = max(ends[start], end)
        
        result = []
        curr_start, curr_end = -1, -1
        for i in range(len(ends)):
            if ends[i]:
                if curr_start == -1:
                    curr_start = i
                    curr_end = ends[i]
                else:
                    curr_end = max(curr_end, ends[i])
            
            if i == curr_end:
                result.append([curr_start, curr_end])
                curr_start, curr_end = -1, -1
        
        if curr_start != -1:
            result.append([curr_start, curr_end])

        return result

        """ sorted

        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda i: i[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            start, stop = intervals[i]
            prev_start, prev_stop = result[-1]
            if start > prev_stop:
                result.append(intervals[i])
            else:
                result[-1] = [
                    min(prev_start, start),
                    max(prev_stop, stop)
                ]
        
        return result
        """

