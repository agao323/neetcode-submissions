class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        TIME: 22:17.64
            - getting a little better, still messy on initial implementation

        backtracking
            - exit conditions: 
                sum == target
                sum > target
                no nums left
            - at each nums n, we can either use n or not use n
        """
        result = []

        def dfs(curr, sum, i) -> None:
            if sum == target:
                result.append(list(curr))
                return
            if sum > target or i >= len(nums):
                return
            
            # reuse this num
            dfs(curr + [nums[i]], sum + nums[i], i)
            # don't use this num
            dfs(curr, sum, i + 1)
        
        dfs([], 0, 0)
        return result