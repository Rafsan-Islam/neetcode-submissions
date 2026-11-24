class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            rows, col = divmod(mid, len(matrix[0]))
            if target == matrix[rows][col]:
                return True
            elif target < matrix[rows][col]:
                r = mid -1
            elif target > matrix[rows][col]:
                l = mid + 1
            
        return False