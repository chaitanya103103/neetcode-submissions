class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float("inf")
        best = 0

        for p in prices:
            if p<min:
                min = p
            else:
                best = max(best,p-min)
        return best