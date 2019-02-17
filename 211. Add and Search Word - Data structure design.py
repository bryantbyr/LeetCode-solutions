# -*- coding: utf-8 -*-
# @Time    : 2019/2/15
# @Author  : qirui
# @FileName: 211. Add and Search Word - Data structure design.py


import collections


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)

# Trie + Backtracking/DFS
class WordDictionary(object):

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

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def backtrack(node, word_left):
            if not word_left:
                if node.isEnd:
                    return True
                else:
                    return False
            char = word_left[0]
            if char == ".":
                for next_node in node.children.values():
                    if backtrack(next_node, word_left[1:]):
                        return True
            elif char in node.children and backtrack(node.children[char], word_left[1:]):
                return True
            return False

        return backtrack(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
param_2 = obj.search("bad")
print(param_2)
