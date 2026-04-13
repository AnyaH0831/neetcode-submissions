class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        seen = []
        for i in range(len(s)):
            
            if s[i] not in closeToOpen:
                seen.append(s[i])
            
            else:

                if seen and closeToOpen[s[i]] == seen[-1]:
                    seen.pop()
                else:
                    return False

        if len(seen) == 0:
            return True
        else:
            return False
                
            
            

