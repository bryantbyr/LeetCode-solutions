# 5. Longest Palindromic Substring.py

# Created by bryantbyr on 20180320
# Time:O(n^2)
# Space:O(n^2)
# DP (Time Limit Exceeded)


# class Solution:

#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         n = len(s)
#         dp = [[False for j in range(n)]for i in range(n)]
#         maxlength = 0
#         start = 0
#         end = 0
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     dp[i][j] = True
#                 elif abs(i - j) == 1 and s[i] == s[j]:
#                     dp[i][j] = True
#                 elif s[i] == s[j]:
#                     dp[min(i, j)][max(i, j)] = dp[min(i, j) + 1][max(i, j) - 1]
#                 if dp[min(i, j)][max(i, j)] == True:
#                     if abs(i - j) + 1 > maxlength:
#                         maxlength = abs(i - j) + 1
#                         start = min(i, j)
#                         end = max(i, j)
#         return s[start:end + 1]

# Learn from discuss on 20180320
# Time:O(n^2)
# Space:O(n^2)
# DP


class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False for j in range(n)]for i in range(n)]
        maxlength = 0
        start = 0
        end = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] == True:
                    if j - i + 1 > maxlength:
                        maxlength = j - i + 1
                        start = i
                        end = j
        return s[start:end + 1]


S = Solution()
s = "babad"
print(S.longestPalindrome(s))
