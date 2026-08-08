class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        binary search to find the right row
        binary search to find the right col
        """

        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows - 1

        def bin_search(row: List[int], target: int) -> bool:
            l, r = 0, len(row) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if row[mid] == target:
                    return True
                
                if target < row[mid]:
                    r = mid - 1
                if target > row[mid]:
                    l = mid + 1
            
            return False
                

        while l <= r:
            mid = l + (r - l) // 2
            start = matrix[mid][0]
            end = matrix[mid][-1]

            if start <= target <= end:
                return bin_search(matrix[mid], target)
            
            if target < start:
                r = mid - 1
            if target > end:
                l + mid + 1
        
        return False