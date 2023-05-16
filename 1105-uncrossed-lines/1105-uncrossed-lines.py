class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        len_nums1=len(nums1)
        len_nums2=len(nums2)
        dp=[[0 for i in range(len_nums2+1)] for j in range(len_nums1+1)]

        for i in range(len_nums1):
            for j in range(len_nums2):
                if nums1[i]==nums2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
        return dp[len_nums1][len_nums2]