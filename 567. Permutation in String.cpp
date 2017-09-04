//567. Permutation in String.cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

//Created by bryantbyr on 20170903
//Time:O(m*n)
//Space:O(m)
//unordered_map
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size())
            return false;
        unordered_map<char, int> m1;
        for (unsigned i = 0; i < s1.size(); ++i)
            m1[s1[i]] += 1;
        for (unsigned i = 0; i < s2.size() - s1.size() + 1; ++i) {
            // cout << i << endl << s2.size()<<"  "<<s1.size()<<"  "<<s2.size() - s1.size() << endl;
            unordered_map<char, int> m2;
            for (unsigned j = i; j < i + s1.size(); j++)
                m2[s2[j]] += 1;
            if (m2 == m1)
                return true;
        }
        return false;
    }
};

//Learn from discuss on 20170904
//Time:O(n)
//Space:O(n)
//Two Pointers (sliding window)
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size())
            return false;
        vector<int> count(26, 0);
        for (int i = 0; i < (int)s1.size(); ++i)
            count[s1[i] - 'a']++;
        int left = 0;
        for (int right = 0; right < (int)s2.size(); ++right) {
            if (--count[s2[right] - 'a'] < 0) {//窗口左移,注意恢复count
                // while (++count[s2[left++] - 'a'] != 0);
                count[s2[left] - 'a']++;
                while (count[s2[left] - 'a'] != 0) {
                    left++;
                    count[s2[left] - 'a']++;
                }
                left++;
            } else {
                if (right - left + 1 == (int)s1.size())
                    return true;
            }
        }
        return false;
    }
};

int main()
{
    Solution S;
    string s1 = "rss", s2 = "hsrossre";
    cout << S.checkInclusion(s1, s2) << endl;
}
