class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        path = set()
        rows,cols = len(grid), len(grid[0])


        def dfs(r,c,path):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in path or grid[r][c] != "1":
                return

            path.add((r,c))
            dfs(r,c+1,path)
            dfs(r,c-1,path)
            dfs(r+1,c,path)
            dfs(r-1,c,path)
        
        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == "1" and (r,c) not in path:
                    island+=1
                dfs(r,c,path)
        return island