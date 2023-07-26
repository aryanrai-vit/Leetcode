from collections import defaultdict
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for val in roads:
            adj[val[0]].append([val[1],val[2]])
            adj[val[1]].append([val[0],val[2]])
        d = [[float("inf"),0] for i in range(n)]
        d[0][0] = 0
        d[0][1] = 1
        q = []
        t2 = 10**9 + 7
        heappush(q,[0,0])
        while q:
            t = heappop(q)
            if t[0]>d[t[1]][0]:
                continue
            for val in adj[t[1]]:
                if d[t[1]][0]+val[1] < d[val[0]][0]:
                    d[val[0]][0] = d[t[1]][0]+val[1]
                    d[val[0]][1] = d[t[1]][1]%t2
                    heappush(q,[d[val[0]][0],val[0]])
                elif d[t[1]][0]+val[1] == d[val[0]][0]:
                    d[val[0]][1] += d[t[1]][1]%t2
        return d[n-1][1]%t2