class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
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

        max_num = max([max(i) for i in intervals])
        counts = [0] * (max_num + 1)

        for start, stop in intervals:
            counts[start] += 1
            counts[stop] -= 1
        
        print(counts)
        result = []
        i = 0
        while i < len(counts):
            if counts[i] > 0:
                curr_sum = counts[i]
                l, r = i, i + 1
                while curr_sum > 0:
                    curr_sum += counts[r]
                    r += 1
                result.append([l, r - 1])
                i = r
            else:
                i += 1
        
        return result

