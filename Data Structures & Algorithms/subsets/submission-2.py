class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        TIME: 
            32:34.33 - backtracking
                - knew solution, but took way too long to implement
            32:40.33 - iterative
        """
        
        """ iterative solution
        """
        result = []
        queue = [([], 0)]
        seen = set()

        while queue:
            curr, i = queue.pop(0)
            
            if tuple(curr) not in seen:
                result.append(curr)
                seen.add(tuple(curr))
            
            if i < len(nums):
                queue.append((curr + [nums[i]], i + 1))
                queue.append((curr, i + 1))
        
        return result


        """ backtracking

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
        """

