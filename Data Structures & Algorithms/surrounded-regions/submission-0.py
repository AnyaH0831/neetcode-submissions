class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col):
            if (min(row,col) < 0
                or row >= ROWS
                or col >= COLS
                or board[row][col] != "O"):

                return 

            board[row][col] = "S"

            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)


        for col in range(COLS):
            if board[0][col] == "O":
                dfs(0,col)

            if board[ROWS-1][col] == "O":
                dfs(ROWS-1,col)

        for row in range(ROWS):
            if board[row][0] == "O":
                dfs(row,0)
            if board[row][COLS-1] == "O":
                dfs(row, COLS-1)


        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"





