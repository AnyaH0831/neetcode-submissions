class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        l = 0
        window = len(s1)
        
        for r in range(window, len(s2)+1):
            # print(s2[l:r])
            if Counter(s1) == Counter(s2[l:r]):
                return True
            
            l += 1

        return False
