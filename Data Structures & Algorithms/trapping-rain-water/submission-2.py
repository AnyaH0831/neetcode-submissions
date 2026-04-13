class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1

        # Max prefix and suffix
        prefix, suffix = [0]*len(height), [0]*len(height)

        curMax = 0
        for i in range(len(height)):
            
            if i == 0:
                prefix[i] = curMax
                
            elif prefix[i-1] > curMax:
                prefix[i] = prefix[i-1]
            else:
                prefix[i] = curMax

            curMax = height[i]
        
        curMax = 0
        for i in range(len(height)-1, -1, -1):
            
            if i == len(height) - 1:
                suffix[i] = curMax
            elif suffix[i+1] > curMax:
                suffix[i] = suffix[i+1]
            else:
                suffix[i] = curMax

            curMax = height[i]

        maxArea = 0
        for i in range(len(height)):
            area = (min(prefix[i], suffix[i]) - height[i])
            # print(area)
            if area > 0:
                maxArea += area
        # print(prefix, suffix)
        
        return maxArea
            
