#171. Excel Sheet Column Number

#Created by bryantbyr on 20180809
#Time:O(N)
#Space:O(1)
#python string/char

# class Solution:
#     def titleToNumber(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         index = len(s)-1
#         result = 0
#         for c in s:
#             result += (ord(c)-ord('A')+1)*pow(26,index)
#             index -= 1
#         return result

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for c in s:
            result *= 26
            result += ord(c)-ord('A')+1
        return result


S = Solution()
print(S.titleToNumber('AB'))
