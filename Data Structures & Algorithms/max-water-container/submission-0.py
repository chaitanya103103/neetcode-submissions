class Solution:
    def maxArea(self, heights: List[int]) -> int:
        arr = []
        max = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            area = min(heights[i],heights[j]) * (j - i)
            arr.append(area)

            if heights[i] < heights[j]:
                i+=1
            else:
                j-= 1
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]

        return max