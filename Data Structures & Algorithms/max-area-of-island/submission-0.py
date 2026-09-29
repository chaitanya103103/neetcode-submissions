class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        path = set()
        rows,cols = len(grid),len(grid[0])
        max_Area = 0

        def dfs(r,c,path):
            if r<0 or r>=rows or c<0 or c>= cols or (r,c) in path or grid[r][c] != 1:
                return 0
            
            path.add((r,c))

            return(1+
                    dfs(r+1,c,path)
                    +dfs(r-1,c,path)
                    +dfs(r,c+1,path)
                    +dfs(r,c-1,path))
        
        max_area = 0

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 or (r,c) not in path:
                    max_area= max(max_area,dfs(r,c,path))
        return max_area