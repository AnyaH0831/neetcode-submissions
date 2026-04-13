class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letters = []
        sList = list(s)
        tList = list(t)

        if len(s) != len(t):
            return False

        # print(sList)
        for letter in sList:
            letters.append(letter)

        # print(letters)
        for letter in tList:
            
            if letter not in letters:
                return False
        
            letters.remove(letter)
            # print(letters)
        
        if len(letters) > 0:
            return False

        return True