class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        def solve(negative):
            if(negative < x):
                return 0
            temp = x
            for i in range(50):
                if(temp <= count[i]):
                    return i-50
                temp -= count[i]
                
        neg = 0
        count = [0] * 50
        for i in range(k):
            if(nums[i] < 0):
                count[nums[i]] += 1
                neg += 1
        ans = [solve(neg)]
        for i in range(k, len(nums)):
            if(nums[i] < 0):
                count[nums[i]] += 1
                neg += 1
            if(nums[i-k] < 0):
                count[nums[i-k]] -= 1
                neg -= 1
            ans.append(solve(neg))
        return ans
            
        
            
            
        