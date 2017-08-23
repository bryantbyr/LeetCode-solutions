//344. Reverse String.cpp
#include <iostream>
#include <algorithm>
using namespace std;

//Created by bryantbyr on 20170823
//Time:O(n)
//Space:O(1)
//string (reverse) (+ STL / + Two Pointers)
class Solution {
public:
    string reverseString(string s) {
        // reverse(s.begin(), s.end());
        // return s;

        int fir = 0;
        int sec = s.size() - 1;
        while (fir < sec)
            swap(s[fir++], s[sec--]);
        return s;

    }
};

int main()
{
    Solution S;
    cout << S.reverseString("hello") << endl;
}
