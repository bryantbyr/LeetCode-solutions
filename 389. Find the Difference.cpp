//389. Find the Difference.cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

//Created by bryantbyr on 20171007
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    char findTheDifference(string s, string t) {
        unordered_map<char, int> map;
        for (char c : s)
            map[c]++;
        for (char c : t) {
            if (map.find(c) != map.end() && map[c] != 0)
                map[c]--;
            else
                return c;
        }
    }
};

//Learn from discuss on 20171007
//Time:O(n)
//Space:O(n)
//Bitwise
class Solution {
public:
    char findTheDifference(string s, string t) {
        char res = 0;
        for (char c : s)
            res ^= c;
        for (char c : t)
            res ^= c;
        return res;
    }
};

//Learn from discuss on 20171007
//Time:O(n)
//Space:O(n)
//Bitwise
class Solution {
public:
    char findTheDifference(string s, string t) {
        vector<int> v(26, 0);
        for (unsigned i = 0; i < s.size(); ++i) {
            v[s[i] - 'a']++;
            v[t[i] - 'a']--;
        }
        v[t[t.size() - 1] - 'a']--;
        for (unsigned i = 0; i < v.size(); ++i) {
            if (v[i] < 0)
                return char(i + 'a');
        }
        return ' ';// not NULL or ''
    }
};

//Created by bryantbyr on 20171007
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    char findTheDifference(string s, string t) {
        vector<int> v(26, 0);
        for (char c : s)
            v[c - 'a']++;
        for (char c : t) {
            v[c - 'a']--;
            if (v[c - 'a'] < 0)
                return c;
        }
        return ' ';// not NULL or ''
    }
};

int main()
{
    Solution S;
    string s = "abcdb";
    string t = "abdcbb";
    cout << S.findTheDifference(s, t) << endl;
}
