class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res=0
        h=[]
        total=0

        for min_n2,n1 in sorted(zip(nums2,nums1),reverse=True):
            if len(h)==k:
                total -= heapq.heappop(h)
            
            total += n1
            heapq.heappush(h,n1)
            
            if len(h)==k:
                res=max(res,min_n2*total)
        return res