//459. Repeated Substring Pattern.cpp
#include <iostream>
using namespace std;

//Created by bryantbyr on 20170913
//Time:O(n^2)
//Sapce:O(1)
//string
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int l = s.size();
        for (int i = 1; i <= l / 2; ++i) {
            if (l % i == 0) {
                string t1 = s.substr(0, i), t2 = s.substr(0, i);
                for (int j = 1; j < l / i; j++)
                    t1.append(t2);
                if (t1 == s)
                    return true;
            }
        }
        return false;
    }
};

int main()
{
    Solution S;
    string s = "abab";
    cout << S.repeatedSubstringPattern(s) << endl;
}
