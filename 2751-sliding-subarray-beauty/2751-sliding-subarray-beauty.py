from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        sl = SortedList()
        n = len(nums)
        ng = 0
        for i in range(k):
            sl.add(nums[i])

        ans = []
        ans.append(min(sl[x - 1], 0))
        
        i, j = 0, k
        
        while j < n:
            sl.discard(nums[i])
            sl.add(nums[j])
            i += 1
            j += 1
            ans.append(min(sl[x - 1], 0))
        
        return ans