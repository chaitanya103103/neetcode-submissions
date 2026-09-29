class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        hash = set()

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in nums:
                if num in hash:
                    continue
                
                curr.append(num)
                hash.add(num)

                dfs(curr)
                curr.pop()
                hash.remove(num)
            
        dfs([])
        return res