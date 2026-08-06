class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        brute force:
            - iterate 3x. O(n^3)
        
        better:
            - sort. O(nlogn)
            - for each element:
                - two sum
            - O(n^2)
            - how to figure out distinct?
        
        can we do better?
            - no

        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
        """
        result = []
        seen = set()

        nums = sorted(nums)
        for i in range(len(nums)):
            target = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    if (nums[i], nums[l], nums[r]) not in seen:
                        result.append([nums[i], nums[l], nums[r]])
                    seen.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                if total < target:
                    l += 1
                if total > target:
                    r -= 1
        
        return result
                    
