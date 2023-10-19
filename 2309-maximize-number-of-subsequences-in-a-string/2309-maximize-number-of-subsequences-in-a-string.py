class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:

        cnt1 = cnt2 = 0
        ttl = 0

        for ch in text:
            if ch == pattern[1]:
                cnt2 += 1
                ttl += cnt1
            if ch == pattern[0]:
                cnt1 += 1
        return ttl + max(cnt1,cnt2)