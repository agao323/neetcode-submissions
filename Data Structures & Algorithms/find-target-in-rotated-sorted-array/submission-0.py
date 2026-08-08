class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        should be similar enough to finding the min in a rotated array

            [5,6,1,2,3,4], target = 4
            [4,5,1,2,3], target = 4

            if nums[mid] == target:
                return mid

            if nums[mid] > target and nums[r] >= target:
                target must be in the right half

            if nums[mid] > target and nums[r] < target:
                target must be in the left half

            if nums[mid] < target and nums[l] > target:
                target must be in the right half

            if nums[mid] < target and nums[l] <= target:
                target must be in the left half
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - 1) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                if nums[r] >= target:
                    l += 1
                if nums[r] < target:
                    r -= 1
            if nums[mid] < target:
                if nums[l] > target:
                    l += 1
                if nums[l] <= target:
                    r -= 1
        
        return -1
