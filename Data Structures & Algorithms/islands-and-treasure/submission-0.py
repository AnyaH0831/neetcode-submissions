class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(row, col):
            if (min(row,col) < 0 
                or row == ROWS 
                or col == COLS
                or (row,col) in visit
                or grid[row][col] == -1):
                return
            visit.add((row,col))
            q.append([row,col])

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == 0:
                    q.append([row,col])
                    visit.add((row,col))


        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addCell(row+1,col)
                addCell(row-1,col)
                addCell(row, col+1)
                addCell(row,col-1)
            dist += 1
