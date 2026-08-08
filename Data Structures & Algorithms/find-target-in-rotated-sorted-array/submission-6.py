import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        should be similar enough to finding the min in a rotated array

        we always know one side is sorted. figure out which side is sorted,
        check if target could be in that range. if not, look at the other side.
        if it is in that range, use that range.

        alternatively, easier to reason through:
            1. find the index of the minimum element
            2. min -> end is one search space, start -> min is the other
            3. determine whether target could fall into one of these
            4. run normal bin search on whichever one it could be in
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        min_index = l
        
        left_space = nums[:min_index]
        right_space = nums[min_index:]

        # print(left_space)
        # print(right_space)

        if left_space and left_space[0] <= target <= left_space[-1]:
            idx = bisect.bisect_left(left_space, target)
            return idx if left_space[idx] == target else -1
            # return self.bin_search(left_space, target)
        if right_space and right_space[0] <= target <= right_space[-1]:
            idx = bisect.bisect_left(right_space, target)
            return min_index + idx if right_space[idx] == target else -1
            # right_search = self.bin_search(right_space, target)
            # if right_search == -1:
            #     return -1
            # return min_index + right_search
        return -1
    
    def bin_search(self, space: List[int], target) -> int:
        print(space)
        if True: return -1
        l, r = 0, len(space) - 1
        while l < r:
            mid = (l + (r - l)) // 2
            if space[mid] == target:
                return mid
            if space[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if space[l] == target:
            return l
        return -1


