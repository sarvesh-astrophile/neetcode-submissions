class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # finding rows
        top, bottom = 0, len(matrix) -1
        while top <= bottom:
            middle = top + (bottom - top) // 2

            if target > matrix[middle][-1]:
                top = middle + 1
            elif target < matrix[middle][0]:
                bottom = middle - 1
            else:
                break

        if not top <= bottom:
            return False

        # finding element
        row = top + (bottom - top) // 2
        l, r = 0, len(matrix[0]) -1
        while l <= r:
            m = l + (r - l) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False