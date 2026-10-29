class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(row, col):
            nonlocal grid, current_area


            if grid[row][col] == 0:
                return 

            grid[row][col] = 0
            current_area += 1

            # other rows
            if row > 0:
                dfs(row-1,col)
            if row < len(grid) - 1:
                dfs(row+1,col)
       
            # other cols
            if col > 0:
                dfs(row,col-1)
            if col < len(grid[row]) - 1:
                dfs(row,col+1)


        maximum_area = 0
        current_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
             
                if grid[row][col] == 1:
                    dfs(row,col)
                    maximum_area = max(current_area,maximum_area)
                    current_area = 0

        return maximum_area



