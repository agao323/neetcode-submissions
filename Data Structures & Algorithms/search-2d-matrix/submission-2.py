class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        TIME: 11:35.16
            - fast enough now at bin search
            - messy implementation though, probably not up to par for senior
        binary search to find the right row
        binary search to find the right col
        """

        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = matrix[mid]

            if row[0] <= target <= row[-1]:
                return self.bin_search(matrix[mid], target)
            
            if target < row[0]:
                r = mid - 1
            if target > row[-1]:
                l = mid + 1
        
        return False
    
    def bin_search(self, cols: List[int], target: int) -> bool:
        l, r = 0, len(cols) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if cols[mid] == target:
                return True
            
            if target < cols[mid]:
                r = mid - 1
            if target > cols[mid]:
                l = mid + 1
        
        return False