class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree=[0]*(n)
        for a,b in edges:
            indegree[b]+=1
        res=[]
        for index,val in enumerate(indegree):
            if val==0:
                res.append(index)
        return res