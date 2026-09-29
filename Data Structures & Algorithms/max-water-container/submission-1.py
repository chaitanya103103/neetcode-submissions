class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights)-1
        area = 0

        while left<right:
            area1 = min(heights[left], heights[right]) * (right-left)

            if area1>area:
                area = area1
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        
        return area
