class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):

                boardvalue = board[r][c]
                
                if boardvalue == ".":
                    continue

                if (boardvalue in rows[r]
                    or boardvalue in cols[c]
                    or boardvalue in squares[(r // 3, c // 3)]):
                    return False

                rows[r].add(boardvalue)
                cols[c].add(boardvalue)
                squares[(r // 3, c // 3)].add(boardvalue)

        return True