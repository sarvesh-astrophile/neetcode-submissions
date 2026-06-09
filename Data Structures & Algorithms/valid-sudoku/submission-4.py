class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                if value in rows[r]:
                    return False
                else:
                    rows[r].add(value)

                if value in cols[c]:
                    return False
                else:
                    cols[c].add(value)

                if value in squares[(r//3, c//3)]:
                    return False
                else:
                    squares[(r//3, c//3)].add(value)

        return True

        