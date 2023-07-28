class Solution:
    def create_lps(self, s):
        lps = [0 for _ in s]
       
        for i in range(1, len(s)):
            x = lps[i-1]
            while s[i] != s[x]:
                if x == 0:
                    x = -1
                    break
                x = lps[x-1]
            lps[i] = x +1

        return lps

    def longestPrefix(self, s: str) -> str:
        lps = self.create_lps(s)
        return s[:lps[-1]]