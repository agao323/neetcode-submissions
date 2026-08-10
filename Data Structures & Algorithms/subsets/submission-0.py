class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        DFS & BFS approaches
        """
        
        """ backtracking

        for n in nums:
            add n
            recurse on rest of nums
            remove n
        """
        result = []
        curr = []

        def dfs(i) -> None:
            if i == len(nums):
                result.append(list(curr))
                return
            
            curr.append(nums[i])
            dfs(i + 1)
            curr.remove(nums[i])
            dfs(i + 1)

        dfs(0)
        return result


