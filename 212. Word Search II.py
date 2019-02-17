# -*- coding: utf-8 -*-
# @Time    : 2019/2/16
# @Author  : qirui
# @FileName: 212. Word Search II.py

import collections


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.isEnd = True


# reference:    https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).
# Trie + Backtracking/DFS
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        def backtrack(node, i, j, path):
            if node.isEnd:
                res.append(path)
                node.isEnd = False

            if i < 0 or i >= m or j < 0 or j >= n:
                return
            tmp = board[i][j]
            # node = node.children[tmp]
            node = node.children.get(tmp)
            if not node:
                return
            board[i][j] = '*'
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                backtrack(node, ni, nj, path + tmp)
            board[i][j] = tmp

        res = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.addWord(word)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                backtrack(node, i, j, "")
        return res


# using extra visited set generally
# class Solution(object):
#     def findWords(self, board, words):
#         """
#         :type board: List[List[str]]
#         :type words: List[str]
#         :rtype: List[str]
#         """
#
#         def backtrack(node, i, j, path):
#             if node.isEnd:
#                 res.append(path)
#                 node.isEnd = False
#
#             if i < 0 or i >= m or j < 0 or j >= n or (i,j) in seen:
#                 return
#             tmp = board[i][j]
#             # node = node.children[tmp]
#             node = node.children.get(tmp)
#             if not node:
#                 return
#             seen.add((i,j))
#             for ni, nj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
#                 backtrack(node, ni, nj, path + tmp)
#             seen.remove((i,j))
#
#         res = []
#         trie = Trie()
#         node = trie.root
#         for word in words:
#             trie.addWord(word)
#         m, n = len(board), len(board[0])
#         seen = set()
#         for i in range(m):
#             for j in range(n):
#                 backtrack(node, i, j, "")
#         return res

if __name__ == '__main__':
    S = Solution()
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    print(S.findWords(board, words))
