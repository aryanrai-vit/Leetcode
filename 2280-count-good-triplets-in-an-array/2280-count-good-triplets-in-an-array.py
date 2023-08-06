class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        res = 0
        m2 = [0] * n
        q = []
        
        for i in range(n):
            m2[nums2[i]] = i
            
        for p1 in range(n):
            p2 = m2[nums1[p1]] 
            idx = bisect.bisect(q, p2) 
            q.insert(idx, p2)
            before = idx
            after = n-1 - p1 - p2 + before
            res += before * after
            
        return res