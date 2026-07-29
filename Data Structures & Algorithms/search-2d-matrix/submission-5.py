class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # finding row
        top, bottom = 0, len(matrix) -1
        while top <= bottom:
            row = top + (bottom - top) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not top <= bottom:
            return False

        row = (top + bottom) // 2

        # finding element
        l, r = 0, len(matrix[0]) -1
        while l <= r:
            mid = l + (r - l) // 2

            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False