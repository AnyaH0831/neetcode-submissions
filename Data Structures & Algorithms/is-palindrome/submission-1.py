class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        
        aStr = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                aStr += s[i]

        # print(aStr)
        for i in range(len(aStr)):

            if len(aStr) % 2 == 0:
                if (aStr[i] != aStr[len(aStr)-i-1]):
                    return False
            else:
                if (i != len(aStr)//2):

                    if (aStr[i] != aStr[len(aStr)-i-1]):
                        return False
        return True