class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        dict = {}

        for n in arr:
            dict[n] = dict.get(n,0) + 1
        for ch in arr:
            if dict[ch] == ch:
                res = max(res,ch)
        return res 
