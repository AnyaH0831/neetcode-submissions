class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        counter = 0
        def dfs(array_idx, idx):
            nonlocal grid
            curr = grid[array_idx][idx]

            if curr == "0":
                return 

            if curr == "1":
                grid[array_idx][idx] = "0"

                if array_idx != 0:
                    dfs(array_idx-1, idx)
                if array_idx < len(grid)-1:
                    dfs(array_idx+1, idx)
                if idx < len(grid[array_idx])-1:
                    dfs(array_idx, idx+1)
                if idx > 0:
                    dfs(array_idx, idx-1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == "1":

                    dfs(i,j)
                    counter += 1

        return counter

            
                
                
