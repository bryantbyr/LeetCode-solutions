//541. Reverse String II.cpp
#include <iostream>
#include <algorithm>
using namespace std;

//Created by bryantbyr on 20170910
//Time:O(n)
//Space:O(1)
//string (reverse())
class Solution {
public:
    string reverseStr(string s, int k) {
        for (unsigned i = 0; i < s.size();) {
            if (i + k < s.size())
                reverse(s.begin() + i, s.begin() + i + k);
            else
                reverse(s.begin() + i, s.end());
            i += 2 * k;
        }
        return s;
    }
};

//Created by bryantbyr on 20170910
//Time:O(n)
//Space:O(1)
//string (reverse())
class Solution {
public:
    string reverseStr(string s, int k) {
        for (unsigned i = 0; i < s.size(); i += 2 * k)
            //reverse(s.begin() + i, (i + k < s.size()) ? (s.begin() + i + k) : s.end());
            reverse(s.begin() + i, min(s.begin() + i + k, s.end()));
        return s;
    }
};

int main()
{
    Solution S;
    string s = "abcdefg";
    int k = 2;
    cout << S.reverseStr(s, k) << endl;
}
