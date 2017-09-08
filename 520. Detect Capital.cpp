//520. Detect Capital.cpp
#include <iostream>
using namespace std;

//Created by bryantbyr on 20170908
//Time:O(n)
//Space:O(1)
//string
class Solution {
public:
    bool detectCapitalUse(string word) {
        int l = word.size();
        if (l == 0)
            return false;
        if ('a' <= word[0] && word[0] <= 'z') {
            for (int i = 0; i < l; i++) {
                if ('A' <= word[i] && word[i] <= 'Z')
                    return false;
            }
        }
        else if (l > 1 && 'A' <= word[1] && word[1] <= 'Z') {
            for (int i = 0; i < l; i++) {
                if ('a' <= word[i] && word[i] <= 'z')
                    return false;
            }
        }
        else if (l > 1 && 'a' <= word[1] && word[1] <= 'z') {
            for (int i = 1; i < l; i++) {
                if ('A' <= word[i] && word[i] <= 'Z')
                    return false;
            }
        }
        return true;
    }
};

//Learn from discuss on 20170908
//Time:O(n)
//Space:O(1)
//string (islower() isupper())
class Solution {
public:
    bool detectCapitalUse(string word) {
        int l = word.size();
        if (l == 0)
            return false;
        if (islower(word[0])) {
            for (int i = 0; i < l; i++)
                if (isupper(word[i]))
                    return false;
        }
        else if (l > 1 && isupper(word[1])) {
            for (int i = 0; i < l; i++)
                if (islower(word[i]))
                    return false;
        }
        else if (l > 1 && islower(word[1])) {
            for (int i = 1; i < l; i++)
                if (isupper(word[i]))
                    return false;
        }
        return true;
    }
};

int main()
{
    Solution S;
    string s = "Google";
    cout << S.detectCapitalUse(s) << endl;
}

