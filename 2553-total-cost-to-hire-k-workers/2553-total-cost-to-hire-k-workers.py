class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q1,q2 =[],[]
        left, right = 0, len(costs)-1
        res=0
        for i in range(k):
            while len(q1) < candidates and left<=right:
               heapq.heappush(q1,costs[left])
               left+=1
               
            while len(q2)<candidates and left<=right:
               heapq.heappush(q2,costs[right])
               right-=1
            
            first= q1[0] if q1 else float('inf')
            last = q2[0] if q2 else float('inf')

            if first<=last:
               res+=first
               heapq.heappop(q1)
            else:
               res+=last
               heapq.heappop(q2)
        return res