class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        cur = 0
        saved = 0
        for num in nums:
            saved |= num & cur
            cur |= num
        
        max_num = 0
        
        for num in nums:
            max_num = max(max_num, saved | (cur & ~num) | num << k)
        return max_num
        