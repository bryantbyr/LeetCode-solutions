//67-Add Binary
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


//Created by bryantbyr on 20170815
//Time:O(max(m,n))
//Space:O(1)
//string基本操作 + bit manipulation
class Solution {
public:
    string addBinary(string a, string b) {
        int l1 = a.size(), l2 = b.size(), m = min(l1, l2);
        int k = 0;
        string r = "";
        for (int i = 0; i < m; ++i)
        {
            r += ((a[l1 - i - 1] - '0') ^ (b[l2 - i - 1] - '0')^k) == 1 ? '1' : '0';
            k = (a[l1 - i - 1] - '0') & (b[l2 - i - 1] - '0')
                ||(a[l1 - i - 1] - '0') & k
                ||(b[l2 - i - 1] - '0') & k;
        }
        if (l1 > l2)
            for (int i = 0; i < l1 - m; ++i)
            {
                r += ((a[l1 - l2 - i - 1] - '0')^k) == 1 ? '1' : '0';
                k = (a[l1 - l2 - i - 1] - '0')&k;
            }
        else
            for (int i = 0; i < l2 - m; ++i)
            {
                r += ((b[l2 - l1 - i - 1] - '0')^k) == 1 ? '1' : '0';
                k = (b[l2 - l1 - i - 1] - '0')&k;
            }
        if (k == 1)
            r += '1';
        reverse(r.begin(), r.end());
        return r;
    }
};

int main()
{
    Solution s;
    string t1 = "110010";
    string t2 = "10111";
    cout << s.addBinary(t1, t2) << endl;
    //int m=(t1[0]-'0')&(t2[0]-'0');
    // int m=t1[0]&t2[0];
    // cout<<m<<endl;
}
