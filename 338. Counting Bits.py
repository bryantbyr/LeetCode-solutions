# 338. Counting Bits.py

# Created by bryantbyr on 20180320
# Time:O(n)
# Space:O(n)
# tag: DP


class Solution:

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        dp = [0, 1]
        m = 2
        n = 0
        while m + n <= num:
            if n == m:
                m *= 2
                n = 0
            dp.append(1 + dp[n])
            if n < m:
                n = n + 1
        return dp

# Learn from discuss on 20180320
# Time:O(n)
# Space:O(n)
# tag: DP


class Solution:

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        dp = [0, 1]
        n = 2
        while n <= num:
            # dp.append(dp[n // 2] + n % 2)
            dp.append(dp[n >> 1] + (n & 1))
            n += 1
        return dp

# Learn from discuss on 20180320
# Time:O(n)
# Space:O(n)
# tag: DP


class Solution:

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        iniArr = [0]
        while len(iniArr) < num + 1:
            iniArr.extend([x + 1 for x in iniArr])
        return iniArr[0:num + 1]

S = Solution()
num = 5
list = S.countBits(num)
for x in list:
    print(x)
