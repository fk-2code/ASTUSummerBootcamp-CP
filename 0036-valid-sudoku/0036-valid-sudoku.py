class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        sq = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                n = board[r][c]
                box = (r // 3, c // 3)
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if box not in sq:
                    sq[box] = set()
                if n in rows[r] or n in cols[c] or n in sq[box]:
                    return False
                rows[r].add(n)
                cols[c].add(n)
                sq[box].add(n)
        return True