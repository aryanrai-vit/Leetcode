class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k =  k
        self.stream=sorted(nums,reverse=True)[:k]
        heapify(self.stream)

    def add(self, val: int) -> int:
        
        if  len(self.stream) < self.k:
            heappush(self.stream,val)
        elif self.stream[0]<=val:
            heappop(self.stream)
            heappush(self.stream,val)
        
        return self.stream[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)