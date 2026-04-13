class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left < right:
            
            m = left + (right - left) //2
        
            # print(left, m, right)
            if nums[m] == target:
                return m
            elif nums[m] >= target:
                right = m
            elif nums[m] < target:
                left = m+1


        return left if (left < len(nums) and nums[left] == target) else -1