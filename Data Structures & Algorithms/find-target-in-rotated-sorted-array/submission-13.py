class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L, R = 0, len(nums)-1

        while L < R:
            M = (L+R)//2

            if nums[M] < nums[R]:
                R = M
            else:
                L = M+1

        # print(L)
        # l, r = 0, len(nums)-1

        if nums[L] <= target <= nums[len(nums)-1]:
    
            l, r = L, len(nums)-1
        else:
            l, r = 0, L
        print(l,r)
        while l<r:

            m = (l+r)//2

            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m
            else:
                return m

        if l < len(nums) and nums[l] == target:
            return l
        elif r < len(nums) and nums[r] == target:
            return r
        else:
            return -1



