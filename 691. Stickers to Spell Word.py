# -*- coding: utf-8 -*-
# @Time    : 2019/2/19
# @Author  : qirui
# @FileName: 691. Stickers to Spell Word.py

# 40 / 100 test cases passed.   Status: Time Limit Exceeded
# Backtracking/DFS
# class Solution(object):
#     def minStickers(self, stickers, target):
#         """
#         :type stickers: List[str]
#         :type target: str
#         :rtype: int
#         """
#
#         def backtrack(used, target):
#             if not target:
#                 self.ans = min(self.ans, used)
#                 return
#             if self.ans == used:
#                 return
#             for stick in stickers:
#                 tmp = []
#                 for s in stick:
#                     if s in target:
#                         tmp.append(s)
#                         target.remove(s)
#                 if tmp:
#                     backtrack(used + 1, target)
#                     for s in tmp:
#                         target.append(s)
#
#         self.ans = float('inf')
#         backtrack(0, list(target))
#         return self.ans if self.ans < float('inf') else -1


import collections

# reference:    https://leetcode.com/problems/stickers-to-spell-word/discuss/161470/My-Python-DFS-Solution
# Backtracking/DFS optimization using defaultdict/Counter
class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """

        def backtrack(index, used, dict):
            if index == N:
                self.ans = min(self.ans, used)
                return
            if self.ans == used:
                return
            if dict[target[index]] >= cnt[target[index]]:
                backtrack(index + 1, used, dict)
            else:
                for stick in stickers:
                    if target[index] in stick:
                        for s in stick:
                            dict[s] += 1
                        backtrack(index + 1, used + 1, dict)
                        for s in stick:
                            dict[s] -= 1

        N = len(target)
        cnt = collections.Counter(target)
        dict = collections.defaultdict(int)
        self.ans = float('inf')
        backtrack(0, 0, dict)
        return self.ans if self.ans < float('inf') else -1


# reference:    https://leetcode.com/problems/stickers-to-spell-word/discuss/161470/My-Python-DFS-Solution
# Backtracking/DFS optimization using Counter
# 典型的DFS(list)问题, 按index遍历list/string。优化需要时间开销一定的技巧, 此处用dict/counter进行优化。
class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """

        def backtrack(index, used):
            if index == N:
                self.ans = min(self.ans, used)
                return
            if self.ans == used:
                return
            if cnt[target[index]] <= 0:
                backtrack(index + 1, used)
            else:
                for stick in stickers:
                    if target[index] in stick:
                        for s in stick:
                            cnt[s] -= 1
                        backtrack(index + 1, used + 1)
                        for s in stick:
                            cnt[s] += 1

        N = len(target)
        cnt = collections.Counter(target)
        self.ans = float('inf')
        backtrack(0, 0)
        return self.ans if self.ans < float('inf') else -1


if __name__ == '__main__':
    S = Solution()
    print(S.minStickers(
        ["and", "pound", "force", "human", "fair", "back", "sign", "course", "sight", "world", "close", "saw", "best",
         "fill", "late", "silent", "open", "noon", "seat", "cell", "take", "between", "it", "hundred", "hat", "until",
         "either", "play", "triangle", "stay", "separate", "season", "tool", "direct", "part", "student", "path", "ear",
         "grow", "ago", "main", "was", "rule", "element", "thing", "place", "common", "led", "support", "mean"]
        , "quietchord"))
