class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = 0
        s = set()

        for i in range(len(nums)):
            if nums[i] in s:
                duplicate = nums[i]
            else:
                s.add(nums[i])

        missing = 0

        for i in range(1,len(nums)+1):
            if i not in s:
                missing = i
            
        return [duplicate,missing]