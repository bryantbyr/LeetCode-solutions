//387. First Unique Character in a String.cpp
#include <iostream>
#include <unordered_map>
using namespace std;

//Created by bryantbyr on 20180306
//Time:O(n^2)
//Space:O(1)
//string
class Solution {
public:
    int firstUniqChar(string s) {
        for (unsigned i = 0; i < s.size(); ++i) {
            unsigned j = 0;
            for (; j < s.size(); ++j) {
                if (i != j && s[i] == s[j])
                    break;
            }
            if (j == s.size())
                return i;
        }
        return -1;
    }
};

//Created by bryantbyr on 20180306
//Time:O(n)
//Space:O(n)
//string + hash table
class Solution {
public:
    int firstUniqChar(string s) {
        int hash[26] = {0};
        for (unsigned i = 0; i < s.size(); ++i) {
            hash[s[i] - 'a']++;
        }
        for (unsigned i = 0; i < s.size(); ++i) {
            if (hash[s[i] - 'a'] == 1)
                return i;
        }
        return -1;
        // unordered_map<char, int> m;
        // for (auto &c : s) {
        //     m[c]++;
        // }
        // for (int i = 0; i < s.size(); i++) {
        //     if (m[s[i]] == 1) return i;
        // }
        // return -1;
    }
};

//Learn from discuss on 20180306
//Time:O(n)
//Space:O(n)
//Hash Table + string
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, pair<int, int>> m;
        for (unsigned i = 0; i < s.size(); ++i) {
            m[s[i]].first = i;
            m[s[i]].second++;
        }
        int res = s.size();
        for (auto &p : m) {
            if (p.second.second == 1)
                res = min(res, p.second.first);
        }
        return res == (int)s.size() ? -1 : res;
    }
};

int main()
{
    Solution S;
    string s = "loveleetcode";
    cout << S.firstUniqChar(s) << endl;
}
