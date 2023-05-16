class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0]*(len(questions)+1)
        for i in reversed(range(len(dp)-1)):
            dp[i] = max(dp[i+1], questions[i][0] + (dp[i+1+questions[i][1]] if i+1+questions[i][1] < len(dp)  else 0))
        return dp[0]