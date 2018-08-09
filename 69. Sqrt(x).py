#69. Sqrt(x)

#Created by bryantbyr on 20180809
#Time:O(log(N))
#Space:O(1)
#Binary Search

import math
class Solution:
    # Time Limit Exceeded
    # def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    # for xx in range(0,int(x/2)+2):
    #     if pow(xx,2) <= x and pow(xx+1,2) > x:
    #         return xx

    def mySqrt(self, x):
        left, right = 0, x
        while (left <= right):
            mid = int(left + (right - left) / 2)
            if pow(mid, 2) <= x and pow(mid + 1, 2) > x:
                return mid
            if pow(mid, 2) < x:
                left = mid + 1
            if pow(mid + 1, 2) > x:
                right = mid - 1


# class Solution:
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         return int(math.sqrt(x))


S = Solution()
print(S.mySqrt(16))
