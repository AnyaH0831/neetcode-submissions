class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        lower, upper = 1, max(piles)

        k = max(piles)
        pileLen = len(piles)

        while lower <= upper:

            m = (lower+upper)//2
            
            hours = 0
            # hour = math.ceil(pileLen/m)
            for p in piles:
                hours += math.ceil(p/m)


            # print(lower, upper, m, hours, pileLen)
            # if hours == h:
            #     if m<k:
            #         k = m
            #     # return m 
            if hours > h:
                lower = m+1
            elif hours <= h:

                if m < k:
                    k = m

                upper = m-1
                
        if (lower == upper) and (hours <= h):
            return lower
        return k