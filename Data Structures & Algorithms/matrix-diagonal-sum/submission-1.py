class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r,c = len(mat) , len(mat[0])
        res = 0
        sum = r - 1
        seen = set()
        for i in range(r):
            for j in range(c):
                if i == j:
                    res += mat[i][j]
                    seen.add((i,j))
                if i + j == sum and (i,j) not in seen:
                    res += mat[i][j]
        return res