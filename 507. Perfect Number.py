#507. Perfect Number

#Created by bryantbyr on 20180813
#Time:O(sqrt(N))
#Space:O(1)
#math
import math
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        temp = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if i == math.sqrt(num):
                    temp += i
                else:
                    temp += (i + num / i)
        return temp == num


S = Solution()
print(S.checkPerfectNumber(6))
