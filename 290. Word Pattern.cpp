//290. Word Pattern.cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <sstream>
using namespace std;

// Created by bryantbyr on 20171012
// Time: O(n)
// Space: O(n)
// Hash Table
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        unordered_map<char, int> m1;
        unordered_map<string, int> m2;
        istringstream is(str);
        string s;
        for (unsigned i = 0; i < pattern.size(); ++i) {
            if (!(is >> s))
                return false;
            if (m1.find(pattern[i]) == m1.end() && m2.find(s) == m2.end())
                m1[pattern[i]] = m2[s] = i;
            else if (m1.find(pattern[i]) != m1.end() && m2.find(s) != m2.end() && m1[pattern[i]] == m2[s])
                continue;
            else
                return false;
        }
        // if (is >> s)
        //     return false;
        // return true;
        return !(is >> s);
    }
};

// Learn from discuss on 20171012
// Time: O(n)
// Space: O(n)
// Hash Table (initialize)
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        unordered_map<char, int> m1;
        unordered_map<string, int> m2;
        istringstream is(str);
        string s;
        for (unsigned i = 0; i < pattern.size(); ++i) {
            if (!(is >> s) || m1[pattern[i]] != m2[s])
                return false;
            // if (m1.find(pattern[i]) == m1.end() && m2.find(s) == m2.end())
            //     m1[pattern[i]] = m2[s] = i;
            m1[pattern[i]] = m2[s] = i + 1;
        }
        return !(is >> s);
    }
};

//Learn from discuss on 20171012
//Time:O(n)
//Space:O(n)
//Hash Table (initialize)
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        unordered_map<char, int> m1;
        unordered_map<string, int> m2;
        istringstream in(str);
        int i = 0, n = pattern.size();
        for (string word; in >> word; ++i) {
            if (i == n || m1[pattern[i]] != m2[word])
                return false;
            m1[pattern[i]] = m2[word] = i + 1;
        }
        return i == n;
    }
};

int main()
{
    Solution S;
    string s = "abba";
    string t = "dog cat cat dog dog";
    cout << S.wordPattern(s, t) << endl;
}
