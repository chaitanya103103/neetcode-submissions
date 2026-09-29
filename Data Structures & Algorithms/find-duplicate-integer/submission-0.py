class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = set()

        for i in nums:
            if i in hm:
                return i
            hm.add(i)
            
