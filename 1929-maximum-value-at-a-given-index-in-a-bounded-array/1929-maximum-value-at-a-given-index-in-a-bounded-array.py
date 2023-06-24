class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        l = 0
        r = maxSum

        while l < r:
            m = (l + r) // 2
            if self.getSum(n, index, m) >= maxSum:
                r = m
            else:
                l = m + 1

        return l if self.getSum(n, index, l) > maxSum else l + 1

    def getSum(self, n: int, index: int, x: int) -> int:
        l = min(index, x - 1)
        r = min(n - index, x)
        lSum = ((x - 1) + (x - 1 - l + 1)) * l // 2
        rSum = (x + (x - r + 1)) * r // 2
        return lSum + rSum