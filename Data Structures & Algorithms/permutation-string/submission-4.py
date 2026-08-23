from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        right = len(s1)
        
        if len(s1) > len(s2) :
            return False
        
        for l in range(len(s2)):

            if Counter(s2[l:right]) == Counter(s1):

                return True
            

            right += 1

        return False
            