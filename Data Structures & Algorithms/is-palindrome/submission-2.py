class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        # print(s, l, r)
        while l < r:
            # print('in')
            if (s[l].isdigit() == False and s[l].isalpha() == False):
                l += 1
                continue
            if (s[r].isdigit() == False and s[r].isalpha() == False):
                r -= 1
                continue
            # print(s[l])
            # print(s[r])
            if (s[l] != s[r]):
                return False

            l += 1
            r -= 1
        return True