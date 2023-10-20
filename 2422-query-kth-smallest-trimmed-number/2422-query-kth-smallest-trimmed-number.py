class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        cache={}
        res=[]
        for k,t in queries:
            if t not in cache:
                cache[t]=sorted([(n[-t:],i) for i,n in enumerate(nums)])
            res.append(cache[t][k-1][1])
        return res