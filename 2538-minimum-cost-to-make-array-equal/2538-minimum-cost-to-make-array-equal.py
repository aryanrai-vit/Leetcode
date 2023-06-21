class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        best= 10**30
        left=0
        right=max(nums)+1

        def calc(t):
            c=0
            for i,x in enumerate(nums):
                c+= abs(x-t)*cost[i]
            return c

        while left+10<right:
            mid1=left+(right-left)//3
            mid2=left+(right-left)*2//3

            if calc(mid1)>calc(mid2):
               left=mid1
            else:
               right=mid2
            print(left,right)
        
        for i in range(left,right+1):
            best=min(best,calc(i))
        return best
            
