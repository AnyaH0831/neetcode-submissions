class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]*len(nums)
        # output = {}

        prefix = [1]*len(nums)
        # j = len(nums) - 1
        for i in range(len(nums)):

            if i == 0:
                prefix[i] *= nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]
 
        # print(prefix)
        suffix = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):

            if i == len(nums)-1:
                suffix[i] *= nums[i]
            else:
                suffix[i] = suffix[i+1] * nums[i]
        # print(suffix)

        for i in range(len(nums)):
            
            if i == 0:
                output[i] *= suffix[1]
            elif i == len(nums)-1:
                output[i] *= prefix[len(nums)-2]
            else:
                output[i] = prefix[i-1] * suffix[i+1]

        return output

            