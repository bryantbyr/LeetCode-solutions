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

//Learn from discuss on 20180307
//Time:O(n)
//Space:O(n)
//string
class Solution {
public:
    string customSortString(string S, string T) {
        int hash[26] = {0};
        for (auto &c : T)
            hash[c - 'a']++;
        string res = "";
        for (auto &c : S) {
            for (int i = hash[c - 'a']; i > 0; i--)
                res += c;
            hash[c - 'a'] = 0;
        }
        for (char c = 'a'; c <= 'z'; c++) {
            for (int i = hash[c - 'a']; i > 0; i--)
                res += c;
        }
        return res;
    }
};

int main()
{
    Solution s;
    string S = "cba";
    string T = "abcd";
    cout << s.customSortString(S, T) << endl;
}
