#367. Valid Perfect Square

#Created by bryantbyr on 20180817
#Time:O(log(N))
#Space:O(1)
#binary search
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # for i in range(1,num+1):
        #     if i**2 == num:
        #         return True
        # return False

        return True if int(num ** 0.5) == (num ** 0.5) else False

        left, right = 1, num
        while (left <= right):
            mid = int(left + (right - left) / 2)
            if (mid ** 2 == num):
                return True
            if (mid ** 2 < num):
                left = mid + 1
            else:
                right = mid - 1
        return False


#Learn from discuss on 20180817
#Time:O(sqrt(N))
#Space:O(1)
#math
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # for i in range(1,num+1):
        #     if i**2 == num:
        #         return True
        # return False

        return True if int(num ** 0.5) == (num ** 0.5) else False


#Learn from discuss on 20180817
#Time:O(sqrt(N))
#Space:O(1)
#math
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while (num > 0):
            num -= i
            i += 2
        return num == 0


S = Solution()
print(S.isPerfectSquare(16))
