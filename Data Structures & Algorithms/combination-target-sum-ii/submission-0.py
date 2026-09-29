class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def trav(i, sum, curr):
            if sum == target:
                res.append(curr[:])
                return
            
            if i >= len(candidates) or sum > target:
                return

            curr.append(candidates[i])

            trav(i+1, sum+ candidates[i], curr)

            curr.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            trav(i+1, sum, curr)

        trav(0,0,[])
        return res