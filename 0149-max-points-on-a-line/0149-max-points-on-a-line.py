class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        d={}
        for i in range(n):
            x,y=points[i][0],points[i][1]
            for j in range(i+1,n):
                x1=x-points[j][0]
                y1=y-points[j][1]
                b=x1*y-y1*x
                d[(y1,x1,b)]=0
        for i in range(n):
            x,y=points[i][0],points[i][1]
            for j in d:
                if j[1]*y==j[0]*x+j[2]:
                        d[j]+=1
        m=1
        for x in d:
            m=max(m,d[x])
        return m

                    
