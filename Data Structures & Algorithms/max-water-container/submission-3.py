class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        left = 0
        r = len(heights) - 1

        while left < r:

            area = min(heights[r], heights[left])*(r-left)

            maxArea = max(area,maxArea)

            if heights[left] <= heights[r]:
                left += 1
            else:
                r -= 1

        return maxArea