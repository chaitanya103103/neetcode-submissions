class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        arr = []

        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):

                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            result = [nums[i],nums[j],nums[k],nums[l]]

                            if result not in arr:
                                arr.append(result)

        return arr