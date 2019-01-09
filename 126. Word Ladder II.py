# -*- coding: utf-8 -*-
# @Time    : 2019/1/8
# @Author  : qirui
# @FileName: 126. Word Ladder II.py

import collections


# 21 / 39 test cases passed. Status: Time Limit Exceeded
# class Solution:
#     def findLadders(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: List[List[str]]
#         """
#
#         if endWord not in wordList:
#             return []
#
#         dict, word_length = collections.defaultdict(list), len(beginWord)
#         for word in wordList:
#             for i in range(word_length):
#                 dict[word[:i] + "_" + word[i + 1:]].append(word)
#         queue = [(beginWord, [beginWord])]
#         res = []
#
#         while queue:
#             word, path = queue.pop(0)
#             if res and len(path) >= len(res[0]):
#                 return res
#             if word not in path[:-1]:
#                 for i in range(word_length):
#                     for nei in dict[word[:i] + "_" + word[i + 1:]]:
#                         if nei == endWord:
#                             res.append(path + [nei])
#                         queue.append((nei, path + [nei]))
#
#         return []


# Time: O(N*len)
# Space: O(N)
# BFS
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        if endWord not in wordList:
            return []

        dict, word_length = collections.defaultdict(list), len(beginWord)
        for word in wordList:
            for i in range(word_length):
                dict[word[:i] + "_" + word[i + 1:]].append(word)
        queue = [(beginWord, [beginWord])]
        res, seen = [], set([beginWord])

        while queue:
            new_queue = []
            tmp = set()
            while queue:
                word, path = queue.pop(0)
                for i in range(word_length):
                    for nei in dict[word[:i] + "_" + word[i + 1:]]:
                        if nei not in seen:
                            tmp.add(nei)
                            if nei == endWord:
                                res.append(path + [nei])
                            new_queue.append((nei, path + [nei]))
            if res:
                return res
            seen |= tmp
            queue = new_queue
        return []


# Time: O(N*len)
# Space: O(N)
# BFS
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        if endWord not in wordList:
            return []

        dict, word_length = collections.defaultdict(list), len(beginWord)
        for word in wordList:
            for i in range(word_length):
                dict[word[:i] + "_" + word[i + 1:]].append(word)
        queue = [(beginWord, [beginWord])]
        res, seen = [], set([beginWord])

        new_queue, tmp = [], set()
        while queue:
            word, path = queue.pop(0)
            for i in range(word_length):
                for nei in dict[word[:i] + "_" + word[i + 1:]]:
                    if nei not in seen:
                        tmp.add(nei)
                        if nei == endWord:
                            res.append(path + [nei])
                        new_queue.append((nei, path + [nei]))
            if not queue:
                if res:
                    return res
                seen |= tmp
                queue = new_queue
                new_queue = []
                tmp = set()
        return []


if __name__ == '__main__':
    S = Solution()
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    print(S.findLadders(beginWord, endWord, wordList))
