class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        top, bottom = 0, len(matrix) -1
        while top <= bottom:
            mid = top + (bottom - top) // 2

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break

        if not (top <= bottom):
            return False

        # finding element
        row = top + (bottom - top) // 2
        l, r = 0, len(matrix[0]) -1
        while l <= r:
            m = l + (r - l) // 2

            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True

        return False