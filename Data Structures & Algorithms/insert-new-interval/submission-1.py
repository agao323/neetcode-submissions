class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        algorithm:
            - go through the list to find the interval to start from
                - we found it when intervals[1] >= newInterval[0]
            - go through the rest of the list where newInterval[1] > intervals[0]
                - first place to stop is where intervals[0] > newInterval[1]
            - O(n) time / O(1) space
            - we can probably optimize this to O(logn) time with two binary searches
        """
        # handle all the initial base cases
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if newInterval[1] <= intervals[0][0]:
            intervals[0][0] = newInterval[0]
            return intervals
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        if newInterval[0] >= intervals[-1][1]:
            intervals[-1][1] = newInterval[1]
            return intervals
        if newInterval[0] <= intervals[0][0] and newInterval[1] >= intervals[-1][1]:
            return [newInterval]

        # handle the case where we don't merge or just merge 1
        for i in range(1, len(intervals)):
            curr, prev = intervals[i], intervals[i - 1]
            # don't merge at all
            if newInterval[0] > prev[1] and newInterval[1] < curr[0]:
                intervals.insert(i, newInterval)
                return intervals
            # merge with just curr
            if newInterval[0] > prev[1] and curr[0] <= newInterval[1] <= curr[1]:
                curr[0] = newInterval[0]
                return intervals
            # merge with just prev
            if prev[0] <= newInterval[0] <= prev[1] and newInterval[1] < curr[0]:
                prev[1] = newInterval[1]
                return intervals
        
        # interval will be merged
        start = 0
        for i in range(len(intervals)):
            l, r = intervals[i][0], intervals[i][1]
            if newInterval[0] > r:
                continue
            if newInterval[0] >= l:
                start = i
                break
        
        stop = 0
        for j in range(len(intervals)):
            l, r = intervals[j][0], intervals[j][1]
            if newInterval[1] <= r:
                stop = j
                break
        
        merged = [[
            min(intervals[start][0], newInterval[0]), 
            max(intervals[stop][1], newInterval[1])
        ]]
        # print(intervals)
        # print(intervals[:start])
        # print(merged)
        # print(intervals[stop + 1:])
        return intervals[:start] + merged + intervals[stop + 1:]




        
