class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        naive
            try starting at every gas station
            return the index that works, or -1

        optimized
            calculate the difference. how much gas remains after
            we go from gas[i] to gas[i + 1]. what does that give us?

            [-1, 0, -1, 3]
            [-1, -1, 1]

            might be something here - if the sum of these
            differences is < 0, probably not possible. you're always
            using more gas than you have access to

            after that it becomes a problem of narrowing down
            where to start:
                - it has to be positive, otherwise you can't move
                  onto the next one
                - at most one solution existing implies that
                  the total difference is at most 1?
                  [1,3,3,2] and [2,2,4,1] -> [-1, 1, -1, 1]
                  which would give us two valid starting points
                  of 1 and 3
                  but this other option has a different of 2,
                  and only one valid starting point. the key here
                  is that the running sum can never become
                  negative

        """

        differences = []
        for i in range(len(cost)):
            differences.append(gas[i] - cost[i])
        
        indices = []
        for i, diff in enumerate(differences):
            if diff > 0:
                indices.append(i)

        print(indices)

        for i in indices:
            cur = i
            tank = gas[i]
            while True:
                # go to next gas station
                tank -= cost[cur]
                if tank < 0:
                    break
                cur += 1
                if cur == i:
                    return cur

                # loop around
                if cur == len(gas):
                    cur = 0
                
                tank += gas[cur]
        
        return -1