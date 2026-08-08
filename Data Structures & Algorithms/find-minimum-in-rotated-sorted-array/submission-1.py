class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        TIME: 40:45
            less than some other questions, but this was really bad.
            knew the solution and still botched the implementation
            took me 35 minutes of stumbling, until I looked at the solution
            for the proper implementation. definitely need to revisit this

        variant of binary search
            - we want to find the location where the order is no longer ascending
            - so the decision point should be:
                look at the following:
                    first, last, mid
                if first < mid < last:
                    it's already sorted, return first
                if first > mid < last:
                    minimum between first and mid
                if first < mid > last:
                    minimum between mid and last

        [2,3,4,5,6,7,8,1]
        [8,1,2,3,4,5,6,7]
        [1,2,3,4,5,6,7,8]
        [6,7,8,1,2,3,4,5]
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]