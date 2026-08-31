class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        TIME:
            17:58 - non-optimal interval approach
            
        this is an intervals problem?
        essentially merge intervals and return length of each interval

        xyxxyzbzbbisl

        x: [0, 3]
        y: [1, 4]
        z: [5, 7]
        b: [6, 9]
        i: [10, 10]
        s: [11, 11]
        l: [12, 12]
        
        after merge: [0, 4], [5, 9], [10, 10], ...
        """

        ranges = {}
        letters = []

        for i, c in enumerate(s):
            if c not in ranges:
                ranges[c] = [i, i]
                letters.append(c)
            else:
                ranges[c][1] = i

        ordered_intervals = [ranges[l] for l in letters]

        merged = [ordered_intervals[0]]
        for i in range(1, len(ordered_intervals)):
            start, end = ordered_intervals[i]
            if start < merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])


        return [(end - start + 1) for start, end in merged]



