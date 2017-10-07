//409. Longest Palindrome.cpp
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
    int longestPalindrome(string s) {
        unordered_map<char, int> map;
        for (char c : s)
            map[c]++;
        int res = 0, odd = 0;
        for (auto it = map.begin(); it != map.end(); ++it) {
            res += it->second / 2 * 2;
            if (it->second % 2 != 0)
                odd = 1;
        }
        return res + odd;
    }
};

//Learn from discuss on 20171007
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    int longestPalindrome(const string& s) {
        vector<bool> counts(127);
        int len = 0;
        int single = 0;
        for (char c : s) {
            if (counts[c]) {
                len += 2;
                single -= 1;
                counts[c] = false;
            } else {
                single += 1;
                counts[c] = true;
            }
        }
        return len + (single > 0);
    }
};

int main()
{
    Solution S;
    string s = "bcccb";
    cout << S.longestPalindrome(s) << endl;
}
