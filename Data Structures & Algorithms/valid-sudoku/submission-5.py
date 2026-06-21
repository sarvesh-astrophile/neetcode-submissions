class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                # for rows
                if board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                else:
                    return False

                # for cols
                if board[i][j] not in cols[j]:
                    cols[j].add(board[i][j])
                else:
                    return False

                # for squares
                if board[i][j] not in squares[(i // 3, j // 3)]:
                    squares[(i // 3, j // 3)].add(board[i][j])
                else:
                    return False


        return True