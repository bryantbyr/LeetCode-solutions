//125. Valid Palindrome.cpp
#include <iostream>
using namespace std;

//Created by bryantbyr on 20170901
//Time:O(n)
//Space:O(1)
//string + Two Pointers
class Solution {
public:
    bool isAlphanumeric(char s) {
        if ((s >= 'a' && s <= 'z') || (s >= 'A' && s <= 'Z') || (s >= '0' && s <= '9'))
            return true;
        return false;
    }
    bool isPalindrome(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (!isAlphanumeric(s[l])) l++;
            if (!isAlphanumeric(s[r])) r--;
            if (isAlphanumeric(s[l]) && isAlphanumeric(s[r]) && toupper(s[l]) != toupper(s[r]))
                return false;
            else if (isAlphanumeric(s[l]) && isAlphanumeric(s[r]) && toupper(s[l]) == toupper(s[r])) {
                l++;
                r--;
            }
        }
        return true;
    }
};

//Learn from discuss on 20170901
//Time:O(n)
//Space:O(1)
//string + Two Pointers (use string function)
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (!isalnum(s[l])) l++;
            if (!isalnum(s[r])) r--;
            if (isalnum(s[l]) && isalnum(s[r]) && toupper(s[l]) != toupper(s[r]))
                return false;
            else if (isalnum(s[l]) && isalnum(s[r]) && toupper(s[l]) == toupper(s[r])) {
                l++;
                r--;
            }
        }
        return true;
    }
};

//Learn from discuss on 20170901
//Time:O(n)
//Space:O(1)
//string + Two Pointers (Be better .1)
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (!isalnum(s[l]))
                l++;
            else if (!isalnum(s[r]))
                r--;
            else if (toupper(s[l]) != toupper(s[r]))
                return false;
            else {
                l++;
                r--;
            }
        }
        return true;
    }
};

//Learn from discuss on 20170901
//Time:O(n)
//Space:O(1)
//string + Two Pointers (Be better .2)
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (!isalnum(s[l])) {
                l++;
                continue;
            }
            if (!isalnum(s[r])) {
                r--;
                continue;
            }
            if (toupper(s[l]) != toupper(s[r]))
                return false;
            l++;
            r--;
        }
        return true;
    }
};

//Created by bryantbyr on 20170901
//Time:O(n)
//Space:O(1)
//string + Two Pointers (another way to write this question likely)
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            while (l < (int)s.size() && !isalnum(s[l]))
                l++;
            while (r >= 0 && !isalnum(s[r]))
                r--;
            if(r<0)
                break;
            if (toupper(s[l]) != toupper(s[r]))
                return false;
            l++;
            r--;
        }
        return true;
    }
};

int main()
{
    Solution S;
    string t = ".,";
    cout << S.isPalindrome(t) << endl;
}
