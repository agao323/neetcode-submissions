class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        backtracking
            - exit conditions: 
                sum == target
                sum > target
                no nums left
            - at each nums n, we can either use n or not use n
        """
        result = []
        seen = set()

        def dfs(curr, sum, i) -> None:
            if sum == target:
                # indices = tuple([c[1] for c in curr])
                # if indices not in seen:
                result.append([c[0] for c in curr])
                    # seen.add(indices)
                return
            if sum > target:
                return
            if i >= len(nums):
                return
            
            # reuse this num
            dfs(curr + [(nums[i], i)], sum + nums[i], i)
            # don't use this num
            dfs(curr, sum, i + 1)
        
        dfs([], 0, 0)
        return result