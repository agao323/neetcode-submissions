class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [[1,5],[2,2],[3,3],[4,4]]
        [[1,2],[1,3],[1,4]]

        rather than "removing" intervals, we figure out how big the
        largest number of intervals we can keep is. so we make each
        interval as small as possible

        track all starts and ends in a map
        {
            1: [2, 3, 4]
            2: [3, 4, 5, 6]
            3: [4]
            5: [6]
        }
        
        then what if we end up with something like this:
        {
            2: [2]
            3: [3]
            1: [5]  <- remove
            5: [6]
            6: [8]
            4: [9]  <- remove
        }
        - sort and go through each (start, end) pair
        - find all pairs where start < curr end
        - if the number ever goes over 1, remove that interval
          and continue
        - if we don't see an overlap, continue

        we should just sort by end time, and remove any where the
        interval's start is less than the last interval's end
        """
        
        intervals.sort(key=lambda pair: pair[1])
        # print(intervals)
        
        result = 0
        temp = [intervals[0]]
        for i in range(1, len(intervals)):
            if temp[-1][1] > intervals[i][0]:
                result += 1
                if temp[-1][1] > intervals[i][1]:
                    temp.append(intervals)
            else:
                temp.append(intervals[i])
        
        # print(temp)

        return result