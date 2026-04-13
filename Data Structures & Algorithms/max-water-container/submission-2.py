class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) - 1

        maxSum = 0
        while left < right:

            height = min(heights[left], heights[right])
            width = right - left
            # print(heights[left], heights[right], width)
            if (height*width) > maxSum:
                maxSum = height*width
                

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1

        return maxSum