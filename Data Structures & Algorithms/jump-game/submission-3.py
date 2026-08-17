class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        can jump backwards

        initial thoughts:
            - dfs through the possible paths, which is jump forward or jump back
            - base case: curr index < 0 or >= len(nums), we're out of bounds
                return False
            - base case: curr index == len(nums) - 1
                return True
            - dfs(curr - curr[i]), dfs(curr + curr[i])
        """
        seen = set()

        def dfs(i):
            if i in seen:
                return False
            seen.add(i)
            if i >= len(nums) - 1:
                return True
            if i < 0 or nums[i] == 0:
                return False
            
            results = [
                dfs(j) for j in range(i - nums[i], i + nums[i] + 1)
            ]
            return any(results)
            
        
        return dfs(0)