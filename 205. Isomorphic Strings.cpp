//205. Isomorphic Strings.cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

//Created by bryantbyr on 20171009
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> map;
        unordered_set<char> set;
        for (int i = 0; i < s.size(); ++i) {
            if (map.find(s[i]) != map.end()) {
                if (map[s[i]] != t[i])
                    return false;
            }
            else {
                if (set.find(t[i]) != set.end())
                    return false;
                map[s[i]] = t[i];
            }
            set.insert(t[i]);
        }
        return true;
    }
};

//Learn from discuss on 20171011
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int m1[256] = {0}, m2[256] = {0};
        for (unsigned i = 0; i < s.size(); ++i) {
            if (m1[s[i]] != m2[t[i]])
                return false;
            m1[s[i]] = m2[t[i]] = i + 1;
        }
        return true;
    }
};

//Learn from discuss on 20171011
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, int> m1, m2;
        for (unsigned i = 0; i < s.size(); ++i) {
            if (m1.find(s[i]) == m1.end() && m2.find(t[i]) == m2.end())
                m1[s[i]] = m2[t[i]] = i;
            else if (m1.find(s[i]) != m1.end() && m2.find(t[i]) != m2.end() && m1[s[i]] == m2[t[i]])
                continue;
            else
                return false;
        }
        return true;
    }
};

int main()
{
    Solution S;
    string s = "ab";
    string t = "aa";
    cout << S.isIsomorphic(s, t) << endl;
}
