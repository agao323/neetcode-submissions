class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        TIME:
            3:47.62 - remembered solution from before, not hard to implement
                      because there's no edge cases here

        initial thoughts:
            - two pointer solution. one starts left, one starts right
            - if target too big, move left forward
            - if target too small, move right back
            - if left == right, no target (but question says always one valid solution)
        """

        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            if total < target:
                l += 1
            if total == target:
                return [l + 1, r + 1]
        
        return []
        
