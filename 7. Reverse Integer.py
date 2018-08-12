#7. Reverse Integer

#Created by bryantbyr on 20180812
#Time:O(N)
#Space:O(1)
#math
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x >= 0:
        #     if int(str(x)[::-1]) >= pow(2, 31):
        #         return 0
        #     else:
        #         return int(str(x)[::-1])
        # else:
        #     if -int(str(-x)[::-1]) < -pow(2, 31):
        #         return 0
        #     else:
        #         return -int(str(-x)[::-1])
        result = ((x > 0) - (x < 0)) * int(str(abs(x))[::-1])
        return result if result >= -2 ** 31 and result < 2 ** 31 else 0


S = Solution()
print(S.reverse(-142))
