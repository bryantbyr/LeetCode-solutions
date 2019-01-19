# -*- coding: utf-8 -*-
# @Time    : 2019/1/17
# @Author  : qirui
# @FileName: 854. K-Similar Strings.py


# BFS
# 9 / 54 test cases passed. Status: Time Limit Exceeded
# class Solution(object):
#     def kSimilarity(self, A, B):
#         """
#         :type A: str
#         :type B: str
#         :rtype: int
#         """
#
#         # to_swap_index = [i for i in range(len(A)) if A[i] != B[i]]
#         # A = "".join([char for idx, char in enumerate(A) if idx in to_swap_index])
#         # B = "".join([char for idx, char in enumerate(B) if idx in to_swap_index])
#
#         # A = "".join([a for a, b in zip(A, B) if a != b])
#         # B = "".join([b for a, b in zip(A, B) if a != b])
#
#         A_chars, B_chars = [], []
#         for a, b in zip(A, B):
#             if a != b:
#                 A_chars.append(a)
#                 B_chars.append(b)
#         A = "".join(A_chars)
#         B = "".join(B_chars)
#
#         def get_neighbors(s):
#             return [s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:] for i in range(len(s) - 1) for j in
#                     range(i + 1, len(s))]
#
#         queue, res, seen = [A], 0, set([A])
#         while queue:
#             new_queue = []
#             for s in queue:
#                 if s == B:
#                     return res
#                 for nei in get_neighbors(s):
#                     if nei not in seen:
#                         seen.add(nei)
#                         new_queue.append(nei)
#             queue = new_queue
#             res += 1

# 21 / 54 test cases passed. Status: Time Limit Exceeded
# class Solution(object):
#     def kSimilarity(self, A, B):
#         """
#         :type A: str
#         :type B: str
#         :rtype: int
#         """
#
#         A_chars, B_chars = [], []
#         for a, b in zip(A, B):
#             if a != b:
#                 A_chars.append(a)
#                 B_chars.append(b)
#         A = "".join(A_chars)
#         B = "".join(B_chars)
#
#         def get_neighbors(s):
#             res = []
#             for i in range(len(s) - 1):
#                 for j in range(i + 1, len(s)):
#                     if s[i] == B[i]:
#                         continue
#                     if s[i] == B[j]:
#                         res.append(s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
#             return res
#
#         queue, res, seen = [A], 0, set([A])
#         while queue:
#             new_queue = []
#             for s in queue:
#                 if s == B:
#                     return res
#                 for nei in get_neighbors(s):
#                     if nei not in seen:
#                         seen.add(nei)
#                         new_queue.append(nei)
#             queue = new_queue
#             res += 1


# Learn from discuss
# BFS optimization (to find the first mismatch index)
class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        # A_chars, B_chars = [], []
        # for a, b in zip(A, B):
        #     if a != b:
        #         A_chars.append(a)
        #         B_chars.append(b)
        # A = "".join(A_chars)
        # B = "".join(B_chars)

        def get_neighbors(s, mismatch):
            # res = []
            # for i in range(mismatch + 1, len(s)):
            #     if s[i] != B[i] and s[i] == B[mismatch]:
            #         res.append(s[:mismatch] + s[i] + s[mismatch + 1:i] + s[mismatch] + s[i + 1:])
            # return res

            return [s[:mismatch] + s[i] + s[mismatch + 1:i] + s[mismatch] + s[i + 1:]
                    for i in range(mismatch + 1, len(s)) if s[i] != B[i] and s[i] == B[mismatch]]

        queue, res, seen = [A], 0, set([A])
        while queue:
            new_queue = []
            for s in queue:
                if s == B:
                    return res
                # to find the first mismatch index then fix that
                mismatch = 0
                for i in range(len(A)):
                    if s[i] != B[i]:
                        mismatch = i
                        break

                for nei in get_neighbors(s, mismatch):
                    if nei not in seen:
                        seen.add(nei)
                        new_queue.append(nei)
            queue = new_queue
            res += 1


# BFS optimization
class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        # A_chars, B_chars = [], []
        # for a, b in zip(A, B):
        #     if a != b:
        #         A_chars.append(a)
        #         B_chars.append(b)
        # A = "".join(A_chars)
        # B = "".join(B_chars)

        def get_neighbors(s):
            res = []
            for i in range(len(s) - 1):
                if s[i] == B[i]:
                    continue
                for j in range(i + 1, len(s)):
                    if s[j] != B[j] and s[j] == B[i]:
                        res.append(s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
                break
            return res

        queue, res, seen = [A], 0, set([A])
        while queue:
            new_queue = []
            for s in queue:
                if s == B:
                    return res
                for nei in get_neighbors(s):
                    if nei not in seen:
                        seen.add(nei)
                        new_queue.append(nei)
            queue = new_queue
            res += 1


if __name__ == '__main__':
    S = Solution()
    A = "abcdeabcdeabcdeabcde"
    B = "aaaabbbbccccddddeeee"
    print(S.kSimilarity(A, B))
