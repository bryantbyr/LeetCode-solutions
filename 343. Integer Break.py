#343. Integer Break

#Learn from solution on 20181017
#Time:O(N^2)
#Space:O(1)
#DP + Math
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                # dp[i] = max(max(j, dp[j]) * max(i - j, dp[i - j]), dp[i])
                dp[i] = max(j * max(dp[i - j], (i - j)), dp[i])
        return dp[-1]


s = Solution()
print(s.integerBreak(10))
