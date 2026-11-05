class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def dfs(row, col, i):

            if i == len(word):
                return True
            
            if word[i] != board[row][col]:
                return False

            temp = board[row][col]
            board[row][col] = '#'

            found = False
            if row > 0:
                found = found or dfs(row-1, col, i+1)

            if row < len(board)-1:
                found = found or dfs(row+1, col, i+1)

            if col > 0:
                found = found or dfs(row, col-1, i+1)

            if col < len(board[row])-1:
                found = found or dfs(row, col+1, i+1)
            
            board[row][col] = temp
            return found

        if len(board) == 1 and len(board[0]) == 1:
            return (word == board[0][0])
        for row in range(len(board)):
            for col in range(len(board[row])):

                if board[row][col] == word[0]:
                    
                    if dfs(row, col, 0):
                        return True


        return False