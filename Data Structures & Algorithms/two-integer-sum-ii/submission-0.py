class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # aMap = {}
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            
            # mid = (left + right) // 2
            # if numbers[right] > target:
            #     right -= 1
            
            if numbers[right] + numbers[left] > target:
                right -= 1
            
            if numbers[right] + numbers[left] < target:
                left += 1

            if numbers[right] + numbers[left] == target:
                return [left+1, right+1]