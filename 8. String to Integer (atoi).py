# -*- coding: utf-8 -*-
# @Time    : 2019/2/28
# @Author  : qirui
# @FileName: 8. String to Integer (atoi).py

# string
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        start, end = -1, -1
        for i in range(len(str)):
            if start == -1:
                if str[i] in ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    start = i
                elif str[i] != ' ':
                    return 0
            elif str[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                end = i
                break
        if start == -1:
            return 0
        if end == -1:
            end = len(str)

        # digits_str = str[start:end]
        # ans, base = 0, 1
        # for digit in reversed(digits_str):
        #     if digit == '-':
        #         ans = -ans
        #     elif digit != '+':
        #         ans += (ord(digit) - ord('0')) * base
        #         base *= 10

        # ans, base = 0, 1
        # for index in range(end - 1, start - 1, -1):
        #     if str[index] == '-':
        #         ans = -ans
        #     elif str[index] != '+':
        #         ans += (ord(str[index]) - ord('0')) * base
        #         base *= 10

        base = 0
        sign = -1 if str[start] == '-' else 1
        start += (1 if str[start] in ['+', '-'] else 0)
        for index in range(start, end):
            base = (ord(str[index]) - ord('0')) + base * 10
        ans = sign * base

        if ans < -2147483648:
            ans = -2147483648
        elif ans > 2147483647:
            ans = 2147483647
        return ans

# string (once loop)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        sign, base = 0, 0
        for i in range(len(str)):
            # 第一个字符不是'+'/'-'或数字, 跳出遍历循环
            if sign == 0 and str[i] not in [' ', '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break
            # 第一个数字字符串遍历完毕, 跳出循环
            if sign != 0 and str[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break
            # 确定符号
            if sign == 0:
                if str[i] == '-':
                    sign = -1
                elif str[i] == '+' or str[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    sign = 1
            # 累加数字
            if str[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                base = (ord(str[i]) - ord('0')) + base * 10
                if base * sign < -2147483648:   # 即时判断是否溢出
                    return -2147483648
                elif base * sign > 2147483647:
                    return 2147483647
        return sign * base


if __name__ == '__main__':
    S = Solution()
    print(S.myAtoi("-42"))
