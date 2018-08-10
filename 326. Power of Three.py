#326. Power of Three

#Created by bryantbyr on 20180810
#Tiem:O(log(N))
#Space:O(1)
#math

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = 1
        while (temp < n):
            temp *= 3
        return temp == n


S = Solution()
print(S.isPowerOfThree(9))
