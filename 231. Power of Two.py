#231. Power of Two

#Created by bryantbyr on 20180810
#Time:O(log(N))
#Space:O(1)
#math
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        while(True):
            if n == 1:
                return True
            if n%2 != 0:
                return False
            n = n/2


#Learn from discuss on 20180810
#Time:O(log(N))
#Space:O(1)
#bit manipulation
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n != 0 and not (n & (n-1))


S=Solution()
print(S.isPowerOfTwo(2))
