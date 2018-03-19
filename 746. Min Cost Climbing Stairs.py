# 746. Min Cost Climbing Stairs.py

# Created by bryantbyr on 20180319
# Time:O(n)
# Space:O(n)
# tag: DP + array


class Solution:

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        m = len(cost)
        dp = []
        for i in range(m):
            if i == 0:
                dp.append(cost[0])
            elif i == 1:
                dp.append(cost[1])
            else:
                dp.append(min(cost[i] + dp[i - 2], cost[i] + dp[i - 1]))
        return min(dp[m - 1], dp[m - 2])

# Learn from discuss on 20180319
# Time:O(n)
# Space:O(n)
# tag: DP + array


# class Solution:

#     def minCostClimbingStairs(self, cost):
#         n = len(cost)
#         minCost0, minCost1 = cost[0], cost[1]
#         for i in range(2, n):
#             minCost0, minCost1 = minCost1, min(minCost0, minCost1) + cost[i]
#         return min(minCost0, minCost1)

S = Solution()
cost = [10, 15, 20]
print(S.minCostClimbingStairs(cost))
