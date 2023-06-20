class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        avgs=[-1 for _ in range(n)]

        for i in range(1,n):
            nums[i]+=nums[i-1]
        for i in range(k,n):
            if (k+i)>=n:
                break
            if k==i:
                avgs[i]=nums[k+i]//(2*k+1)
            else:
                avgs[i]=(nums[k+i]-nums[i-k-1])//(2*k+1)
        return avgs