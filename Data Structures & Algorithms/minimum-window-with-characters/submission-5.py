class Solution:

    def get_idx(self, char: str) -> int:
        if 'a' <= char <= 'z':
            return ord(char) - ord('a')
        return ord(char) - ord('A') + 26

    def check_match(self, tCount, winCount):
        for val_t, val_win in zip(tCount, winCount):
            if val_t != 0:
                if val_t > val_win:
                    return False
        return True

    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        if s == t:
            return t

        tCount = [0] * 52
        need = 0
        for char in t:
            index = self.get_idx(char)
            if tCount[index] == 0:
                need += 1
            tCount[index] += 1

        winCount = [0] * 52
        have = 0

        minLen = len(s) + 1
        bestL, bestR = 0, 0
        l = 0

        for r in range(len(s)):

            r_idx = self.get_idx(s[r])
            winCount[r_idx] += 1

            if tCount[r_idx] > 0 and winCount[r_idx] == tCount[r_idx]:
                have += 1
            while have == need:
                window_len = r - l + 1
                if window_len < minLen:
                    minLen = window_len
                    bestL, bestR = l, r+1
                l_idx = self.get_idx(s[l])
                winCount[l_idx] -= 1

                if tCount[l_idx] > 0 and winCount[l_idx] < tCount[l_idx]:
                    have -= 1
                l += 1

        return s[bestL:bestR] if minLen < len(s) + 1 else ""