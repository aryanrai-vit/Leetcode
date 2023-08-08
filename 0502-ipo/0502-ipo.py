class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort()
        heap = []
        for _ in range(k):
            while projects and projects[0][0] <= w:
                capital, profit = projects.pop(0)
                heapq.heappush(heap, -profit)
            if not heap:
                break    
            w -= heapq.heappop(heap)
        return w