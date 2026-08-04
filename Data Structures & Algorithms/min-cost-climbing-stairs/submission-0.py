class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # maintain an array with the running min costs
        # at each point, can take i+1 or i+2
        # arry[i+1] -> cost[i+1] + min(cost[i-1], cost[i-2])

        """
        edge cases:
             - len(cost) == 0, 1
             - can costs be negative?
             - cost numbers too big
        """
        min_costs = [0] * len(cost)
        min_costs[0], min_costs[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            min_costs[i] = cost[i] + min(min_costs[i - 1], min_costs[i - 2])

        return min(min_costs[-1], min_costs[-2])