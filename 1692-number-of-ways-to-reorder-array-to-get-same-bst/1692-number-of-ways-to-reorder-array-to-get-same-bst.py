class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9 + 7 
        
        def cntways(array):
            if len(array) <= 2:
                return 1
            left = [v for v in array if v < array[0]]
            right = [v for v in array if v > array[0]]
            return comb(len(left) + len(right), len(right))*cntways(left)*cntways(right)
        
        return (cntways(nums) - 1)%mod