class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        # Last index of each character

        # start of the window
        l = 0

        # Longest length
        res = 0

        for r in range(len(s)):

            if s[r] in mp:
                l = max(mp[s[r]] + 1,l)

            mp[s[r]] = r

            res = max(res, r-l+1)

        return res