//557. Reverse Words in a String III.cpp
#include <iostream>
#include <algorithm>
using namespace std;

//Created by bryantbyr on 20170909
//Time:O(n)
//Space:O(1)
//string
class Solution {
public:
    string reverseWords(string s) {
        for (unsigned i = 0; i < s.size(); ++i) {
            unsigned j = i;
            while (j < s.size() && s[j] != ' ')
                j++;
            unsigned temp = j--;
            while (i < j)
                swap(s[i++], s[j--]);
            i = temp;
        }
        return s;
    }
};

//Learn from discuss on 20170909
//Time:O(n)
//Space:O(1)
//string (reverse())
class Solution {
public:
    string reverseWords(string s) {
        for (unsigned i = 0; i < s.size(); ++i) {
            unsigned j = i;
            while (j < s.size() && s[j] != ' ')
                j++;
            reverse(s.begin() + i, s.begin() + j);
            i = j;
        }
        return s;
    }
};

int main()
{
    Solution S;
    string s = "Let's take LeetCode contest";
    cout << S.reverseWords(s) << endl;
}
