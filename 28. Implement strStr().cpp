//28. Implement strStr().cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170901
//Time:O(n*m)
//Space:O(1)
//Two Pointers + substr
class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.size(), n = needle.size();
        // if(n==0)
        //     return 0;
        for (int i = 0; i < m - n + 1; i++) {
            int j = 0;
            for (; j < n; j++) {
                if (haystack[i + j] != needle[j])
                    break;
            }
            if (j == n)
                return i;
        }
        return -1;
    }
};

//Learn from discuss on 20170901
//Time:O(n*m)
//Space:O(1)
//string + substr
class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.size(), n = needle.size();
        // if(n==0)
        //     return 0;
        for (int i = 0; i < m - n + 1; i++) {
            if(haystack.substr(i,n)==needle)
                return i;
        }
        return -1;
    }
};

int main()
{
    Solution S;
    string t = "abcdebcf";
    string s = "deb";
    cout << S.strStr(t, s) << endl;
    return 0;
}
