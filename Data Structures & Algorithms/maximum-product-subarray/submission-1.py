class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currmin = 1
        currmax = 1

        for n in nums:
            if n == 0:
                currmin , currmax = 1,1
                continue
            temp = currmax * n
            currmax = max(currmax*n,currmin*n,n)
            currmin = min(temp, currmin*n, n)

            res = max(currmin,currmax,res)
        return res
