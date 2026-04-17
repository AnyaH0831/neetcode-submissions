class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import math
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1)

        while l <= r:

            m = (l+r)//2
            idx = (len(nums1)+len(nums2))//2 - m

            left1 = nums1[m-1] if m > 0 else float('-inf')
            right1 = nums1[m] if m < len(nums1) else float('inf')
            
            left2 = nums2[idx-1] if idx > 0 else float('-inf')
            right2 = nums2[idx] if idx < len(nums2) else float('inf')

            if left1 <= right2 and left1 <= right1:
                if (len(nums1)+len(nums2))%2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2)+min(right1,right2))/2

            elif left1 > left2:
                r = m- 1
            else:
                l = m+ 1
    