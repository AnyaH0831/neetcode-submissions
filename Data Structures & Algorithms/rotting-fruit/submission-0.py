class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        ROWS, COLS = len(grid), len(grid[0])

        visit = set()
        q = deque()

        def addCell(row, col):
            nonlocal fresh
            if (min(row,col) < 0
                or row == ROWS
                or col == COLS
                or (row,col) in visit
                or grid[row][col] == 0):
                return

            visit.add((row,col))
            q.append([row,col])
            fresh -= 1

        fresh = 0
        for row in range(ROWS):
            for col in range(COLS):

                if grid[row][col] == 2:
                    q.append([row,col])
                    visit.add((row,col))
                elif grid[row][col] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        time = 0
        while q:

            for i in range(len(q)):

                row, col = q.popleft()

                grid[row][col] = 2

                addCell(row-1,col)
                addCell(row+1,col)
                addCell(row,col-1)
                addCell(row,col+1)
            if q:
                time += 1

        return time if fresh == 0 else -1
