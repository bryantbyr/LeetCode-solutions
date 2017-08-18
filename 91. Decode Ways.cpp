//91. Decode Ways.cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

//Created by bryantbyr on 20170818
//Time:O(n)
//Space:O(n)
//DP(+string基本操作)
class Solution {
public:
    int numDecodings(string s) {
        int l = s.size();
        if (l == 0 || s[0] == '0')
            return 0;
        vector<int> v(l + 1, 0);
        v[0] = v[1] = 1;
        for (int i = 2; i <= l; i++) {
            if ("10" <= s.substr(i - 2, 2) && s.substr(i - 2, 2) <= "26")//'10'!="10"
                v[i] = v[i - 2];
            if (s[i - 1] != '0')
                v[i] += v[i - 1];
        }
        return v[l];
    }
};

int main()
{
    Solution s;
    string t = "12";
    cout << s.numDecodings(t) << endl;
}
