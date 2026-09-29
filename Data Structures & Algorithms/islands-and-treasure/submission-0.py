class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        INF = 2147483647
        rows,cols = len(grid),len(grid[0])
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            row,col = queue.popleft()
            for dr,dc in directions:
                r, c = row+dr, col+dc

                if 0<= r < rows and 0<= c < cols and grid[r][c] == INF:
                    grid[r][c] = grid[row][col] + 1
                    queue.append((r,c))