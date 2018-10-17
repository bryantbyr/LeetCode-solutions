#96. Unique Binary Search Trees

#Learn from solution on 20181017
#Time:O(n^2)
#Space:O(n)
#Tree + DP
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[i - j] * dp[j - 1]
        return dp[-1]


s = Solution()
print(s.numTrees(3))
