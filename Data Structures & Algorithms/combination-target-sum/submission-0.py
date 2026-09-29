class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def trav(i, sum, curr):
            if sum == target:
                res.append(curr.copy())
                return

            
            if i >= len(nums) or sum > target:
                return
            

            curr.append(nums[i])

            trav(i, sum+nums[i], curr)

            curr.pop()

            trav(i+1, sum, curr)
        
        trav(0,0,[])
        return res