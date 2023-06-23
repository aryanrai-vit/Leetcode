class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        N=len(nums)
        best=1

        lookup=collections.defaultdict(lambda:1)
        for start in range(N):
            for i in range(start+1,N):
                delta=nums[i]-nums[start]
                lookup[(nums[i],delta)]=lookup[(nums[start],delta)]+1
                if delta !=0:
                    best=max(best,lookup[(nums[i],delta)])
        return max(best,max(collections.Counter(nums).values()))