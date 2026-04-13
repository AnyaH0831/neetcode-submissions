class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        m = (left+right)//2
        while left < right:

            m = (left+right)//2

            if nums[m] < nums[right]:
                right = m
            else:
                left = m+1

        
        if nums[right] < nums[m]:
            return nums[right]
        else:
            return nums[m]