class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m,n = len(matrix),len(matrix[0])
        right = m*n-1
        while left <= right:
            middle = (left + right) // 2
            midrow,midcol = divmod(middle,n)
            if matrix[midrow][midcol] == target:
                return True
            elif matrix[midrow][midcol] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False


