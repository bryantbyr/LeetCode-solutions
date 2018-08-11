#9. Palindrome Number

#Created by bryantbyr on 20180811
#Time:O(N)
#Space:O(1)
#math
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        temp = 0
        origin = x
        while (x != 0):
            temp = temp * 10 + x % 10
            x = int(x / 10)
        return origin == temp

#Learn from discuss on 20180811
#Time:O(N)
#Space:O(1)
#math
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # x_list = [i for i in str(x)]
        # return x_list == x_list[::-1]

        return str(x) == str(x)[::-1]


S = Solution()
print(S.isPalindrome(121))
