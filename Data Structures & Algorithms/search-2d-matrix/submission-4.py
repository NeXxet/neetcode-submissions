class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # formula for getting equivalent position from matrix
        # if numbers were in a single list
        # (len(matrix[0]) * matrix row) + matrix column

        # formula to convert numLineIndex to matrix representation
        # row = numLineIndex // cols
        # col = numLineIndex % cols

        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (high+low)//2

            mid_cell = matrix[mid//cols][mid%cols]

            if mid_cell < target:
                low = mid + 1
            elif mid_cell > target:
                high = mid - 1
            else:
                return True

        return False