//242-Valid Anagram.cpp
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

/**
 * 20170409
 * Time:O(NlogN)
 * Space:O(1))
 * 排序，然后比较
 */
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
