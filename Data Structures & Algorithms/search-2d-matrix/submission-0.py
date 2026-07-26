class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # formula for getting equivalent position from matrix
        # if numbers were in a single list
        # (len(matrix[0]-1) * matrix row) + matrix column

        # formula to convert numLineIndex to matrix representation
        # row = numLineIndex // rowSize
        # col = numLineIndex % rowSize

        def getNumLineIndex(rowSize, row, col):
            return ((rowSize)*row) + col
        
        def rowIndex(numLineIndex, rowSize):
            return numLineIndex // rowSize

        def colIndex(numLineIndex, rowSize):
            return numLineIndex % rowSize

        rowSize = len(matrix[0])

        low = 0
        high = (rowSize * len(matrix)) - 1

        while low <= high:
            mid = (high+low)//2

            midCell = matrix[rowIndex(mid, rowSize)][colIndex(mid, rowSize)]

            if midCell < target:
                low = mid + 1
            elif midCell > target:
                high = mid - 1
            else:
                return True

        return False