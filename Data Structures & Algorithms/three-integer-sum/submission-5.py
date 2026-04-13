class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            curr = nums[i]
            left, right = i+1, len(nums) - 1
            print(curr, nums[i-1])
            if curr > 0:
                break

            if i > 0 and curr == nums[i-1]:
                print("in",curr, nums[i-1])
                continue
            left, right = i+1, len(nums) - 1 
            print(result)
            while left < right:

                total = (nums[left] + nums[right])

                if total + curr == 0:
                    result += [[nums[left], nums[right], curr]]
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                
                elif total + curr > 0:
                    right -= 1
                
                # elif total + curr > 0:
                else:
                    left += 1
        
        # print(result)
        return result
            
