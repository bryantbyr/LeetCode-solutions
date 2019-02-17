# -*- coding: utf-8 -*-
# @Time    : 2019/2/15
# @Author  : qirui
# @FileName: 401. Binary Watch.py

# Backtracking/DFS (general)
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        def backtrack(tmp_h, tmp_m, start):
            if len(tmp_h) + len(tmp_m) == num:
                h, m = sum(tmp_h), sum(tmp_m)
                if h <= 11 and m <= 59:
                    concat_str = ":0" if m < 10 else ":"
                    res.append(str(h) + concat_str + str(m))
                return
            for i in range(start, 10):
                if i < 4:
                    backtrack(tmp_h + [nums[i]], tmp_m, i + 1)
                else:
                    backtrack(tmp_h, tmp_m + [nums[i]], i + 1)

        nums = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        res = []
        backtrack([], [], 0)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.readBinaryWatch(1))
