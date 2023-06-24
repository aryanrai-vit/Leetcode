class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        s_sum = sum(rods)
        dp = [-1] * (s_sum + 1)
        dp[0] = 0

        for rod in rods:
            dp_copy = dp[:]

            for i in range(s_sum - rod + 1):
                if dp_copy[i] < 0:
                    continue

                dp[i + rod] = max(dp[i + rod], dp_copy[i])
                dp[abs(i - rod)] = max(dp[abs(i - rod)], dp_copy[i] + min(i, rod))

        return dp[0]