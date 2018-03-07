//791. Custom Sort String.cpp
#include <iostream>
#include <algorithm>
using namespace std;

//Learn from discuss on 20180307
//Time:O(n*log(n))
//Space:O(1)
//sort + string
class Solution {
public:
    string customSortString(string S, string T) {
        //学习自定义比较函数comp的写法！
        sort(T.begin(), T.end(), [&](char a, char b) {return S.find(a) < S.find(b);});
        return T;
    }
};

int main()
{
    Solution s;
    string S = "cba";
    string T = "abcd";
    cout << s.customSortString(S, T) << endl;
}
