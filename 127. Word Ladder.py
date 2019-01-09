# -*- coding: utf-8 -*-
# @Time    : 2019/1/7
# @Author  : qirui
# @FileName: 127. Word Ladder.py

# 21 / 39 test cases passed. Time Limit Exceeded
# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#
#         queue, seen = [(beginWord, 1)], set()
#         word_length = len(beginWord)
#
#         while queue:
#             word, step = queue.pop(0)
#             seen.add(word)
#             if word == endWord:
#                 return step
#             for i in range(word_length):
#                 for c in "abcdefghijklmnopqrstuvwxyz":
#                     nei = word[:i] + c + word[i + 1:]
#                     if nei in wordList and nei not in seen:
#                         queue.append((nei, step + 1))
#         return 0


# 29 / 39 test cases passed.
# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         if endWord not in wordList:
#             return 0
#
#         queue = [(beginWord, 1)]
#         word_length = len(beginWord)
#
#         while queue:
#             word, step = queue.pop(0)
#             for i in range(word_length):
#                 for c in "abcdefghijklmnopqrstuvwxyz":
#                     nei = word[:i] + c + word[i + 1:]
#                     if nei in wordList:
#                         wordList.remove(nei)
#                         if nei == endWord:
#                             return step + 1
#                         queue.append((nei, step + 1))
#
#         return 0

# Learn from discuss
# Time: O(N*len*26)
# Space: O(N)
# BFS (python set is faster than list)
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        wordList = set(wordList)
        queue = [(beginWord, 1)]
        word_length = len(beginWord)

        while queue:
            word, step = queue.pop(0)
            for i in range(word_length):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nei = word[:i] + c + word[i + 1:]
                    if nei in wordList:
                        wordList.remove(nei)
                        if nei == endWord:
                            return step + 1
                        queue.append((nei, step + 1))
        return 0

import collections

# 30 / 39 test cases passed.
# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         if endWord not in wordList:
#             return 0
#
#         dict, word_length = collections.defaultdict(list), len(beginWord)
#         for word in wordList:
#             for i in range(word_length):
#                 dict[word[:i] + "_" + word[i + 1:]].append(word)
#         queue, seen = [(beginWord, 1)], set()
#
#         while queue:
#             word, step = queue.pop(0)
#             for i in range(word_length):
#                 for nei in dict[word[:i] + "_" + word[i + 1:]]:
#                     if nei not in seen:
#                         if nei == endWord:
#                             return step + 1
#                         seen.add(word)
#                         queue.append((nei, step + 1))
#         return 0

# Learn from discuss
# Time: O(N*len)
# Space: O(N)
# BFS using adjacent list
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        dict, word_length = collections.defaultdict(list), len(beginWord)
        for word in wordList:
            for i in range(word_length):
                dict[word[:i] + "_" + word[i + 1:]].append(word)
        queue, seen = [(beginWord, 1)], set()

        while queue:
            word, step = queue.pop(0)
            if word not in seen:
                seen.add(word)
                for i in range(word_length):
                    for nei in dict[word[:i] + "_" + word[i + 1:]]:
                        if nei == endWord:
                            return step + 1
                        queue.append((nei, step + 1))
        return 0


if __name__ == '__main__':
    S = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(S.ladderLength(beginWord, endWord, wordList))
