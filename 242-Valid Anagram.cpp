//242-Valid Anagram.cpp
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        return s==t;
    }
};

int main()
{
    Solution s;
    string s1="anagram";
    string s2="nagaram";
    cout<<s.isAnagram(s1,s2)<<endl;
    return 0;
}
