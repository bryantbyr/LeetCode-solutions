//567. Permutation in String.cpp
#include <iostream>
#include <unordered_map>
using namespace std;

//Created by bryantbyr on 20170903
//Time:O(m*n)
//Space:O(m)
//unordered_map
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.size()>s2.size())
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

int main()
{
    Solution S;
    string s1 = "ros", s2 = "horse";
    cout << S.checkInclusion(s1, s2) << endl;
}
