class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        res = k

        l,r = 0,0
        while r<len(blocks):
            if blocks[r] == "W":
                count+=1
              
            if r-l+1 == k:
                res = min(count,res)
                if blocks[l] == "W":
                    count -= 1
                l += 1
            r+=1
        return res
