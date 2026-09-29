from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pac = deque()
        p_seen = set()

        atl = deque()
        a_seen = set()

        
        for j in range(cols):
            pac.append((0, j))
            p_seen.add((0, j))

        
        for i in range(rows):
            pac.append((i, 0))
            p_seen.add((i, 0))

        # 3. Atlantic - bottom row
        for j in range(cols):
            atl.append((rows - 1, j))
            a_seen.add((rows - 1, j))

        # 4. Atlantic - right column
        for i in range(rows):
            atl.append((i, cols - 1))
            a_seen.add((i, cols - 1))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def get_coord(que, seen):
            while que:
                row, col = que.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and (nr, nc) not in seen
                            and heights[nr][nc] >= heights[row][col]):   # reverse flow: uphill or equal
                        seen.add((nr, nc))
                        que.append((nr, nc))

        get_coord(pac, p_seen)
        get_coord(atl, a_seen)

        return [[r, c] for r, c in p_seen & a_seen]