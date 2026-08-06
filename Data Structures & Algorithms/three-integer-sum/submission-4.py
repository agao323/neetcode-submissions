class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        TIME: 19:00.71
            - messed up implementation
            - might want to revisit

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
        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            target = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                if total < target:
                    l += 1
                if total > target:
                    r -= 1
        
        return result
                    
