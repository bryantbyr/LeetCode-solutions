//551. Student Attendance Record I.cpp
#include <iostream>
using namespace std;

//Created by bryantbyr on 20170912
//Time:O(n)
//Space:O(1)
//string
class Solution {
public:
    bool checkRecord(string s) {
        int m = 0;
        for (unsigned i = 0; i < s.size(); ++i) {
            if (s[i] == 'A')
                m++;
            if (m > 1)
                return false;
            if (i + 2 < s.size() && s[i] == 'L' && s[i + 1] == 'L' && s[i + 2] == 'L')
                return false;
        }
        return true;
    }
};

//Created by bryantbyr on 20170912
//Time:O(n)
//Space:O(1)
//string
class Solution {
public:
    bool checkRecord(string s) {
        int m = 0;
        for (unsigned i = 0; i < s.size(); ++i) {
            if (s[i] == 'A') {
                m++;
                if (m > 1)
                    return false;
            }
            else if (i + 2 < s.size() && s[i] == 'L' && s[i + 1] == 'L' && s[i + 2] == 'L')
                return false;
        }
        return true;
    }
};

//Learn from discuss on 20170912
//Time:O(n)
//Space:O(1)
//string
class Solution {
public:
    bool checkRecord(string s) {
        int l = 0, a = 0;
        for (unsigned i = 0; i < s.size(); ++i) {
            if (s[i] == 'A')
                a++;
            l = s[i] == 'L' ? l + 1 : 0;
            if (a > 1 || l > 2)
                return false;
        }
        return true;
    }
};

int main()
{
    Solution S;
    string s = "LALL";
    cout << S.checkRecord(s) << endl;
}
