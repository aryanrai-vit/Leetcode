class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nProvince=0
        visited=set()

        def dfs(givenNeighConnections):
            for anotherCity,isInConnection in enumerate(givenNeighConnections):
                if isInConnection and anotherCity not in visited:
                    visited.add(anotherCity)
                    dfs(isConnected[anotherCity])

        for city , neighConnections in enumerate(isConnected):
            if city not in visited:
                nProvince+=1
                dfs(neighConnections)
        
        return nProvince