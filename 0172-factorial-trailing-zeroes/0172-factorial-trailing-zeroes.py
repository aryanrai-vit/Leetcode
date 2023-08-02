class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        log = 5
        while n >= log:
            count += n//log
            log *= 5
        return count