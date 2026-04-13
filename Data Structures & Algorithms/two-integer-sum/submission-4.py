class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        aMap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            

            if difference in aMap:
                return [aMap[difference], i]

            aMap[nums[i]] = i

