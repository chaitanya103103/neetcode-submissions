class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        hm = set()
        duplicate = 0

        for i in nums:
            if i in hm:
                duplicate = i
            else:
                hm.add(i)

        missing = 0

        for i in range(1,len(nums)+1):
            if i not in hm:
                missing = i

        return[duplicate,missing]  
        
