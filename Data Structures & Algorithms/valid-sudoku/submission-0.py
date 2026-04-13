class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)


        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if board[r][c] == '.':
                    continue
                # print(sqrs)
                if (cur in rows[r] or cur in cols[c] or cur in sqrs[(r//3, c//3)]):
                    return False
                
                rows[r].add(cur)
                cols[c].add(cur)
                sqrs[(r//3, c//3)].add(cur)
        return True

