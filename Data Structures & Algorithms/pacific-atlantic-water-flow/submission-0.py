class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []
        visit = set()

        is_pacific = False
        is_atlantic = False
        def dfs(row, col, prev):
            nonlocal is_pacific, is_atlantic

            if (min(row,col) < 0
                or row >= ROWS
                or col >= COLS
                or prev < heights[row][col]
                or (row,col) in visit):

                return 

            if row == 0 or col == 0:
                is_pacific = True

            if row == ROWS-1 or col == COLS-1:
                is_atlantic = True
            visit.add((row,col))
            dfs(row-1,col, heights[row][col])
            dfs(row+1,col,heights[row][col])
            dfs(row,col-1,heights[row][col])
            dfs(row,col+1,heights[row][col])

            

        for row in range(ROWS):
            for col in range(COLS):

                dfs(row, col, 1001)

                if is_pacific and is_atlantic:
                    res.append([row,col])

                is_pacific = False
                is_atlantic = False
                visit = set()

        return res




        