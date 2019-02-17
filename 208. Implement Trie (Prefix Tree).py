# -*- coding: utf-8 -*-
# @Time    : 2019/2/15
# @Author  : qirui
# @FileName: 208. Implement Trie (Prefix Tree).py

import collections


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)


# reference:    https://leetcode.com/articles/implement-trie-prefix-tree/
# Trie (Prefix Tree) + Design
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.isEnd = True

    def searchPrefix(self, word):
        """
        search a prefix or whole key in trie and returns the node where search ends
        :param word: str
        :return: TrieNode
        """

        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.searchPrefix(word)
        return node != None and node.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.searchPrefix(prefix) != None


# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "back"
obj.insert(word)
param_2 = obj.search(word)
print(param_2)
param_3 = obj.startsWith("a")
print(param_3)
