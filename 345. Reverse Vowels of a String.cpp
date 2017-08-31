//345. Reverse Vowels of a String.cpp
#include <iostream>
using namespace std;

//Created by bryantbyr on 20170831
//Time:O(n)
//Space:O(1)
//Two Pointers
class Solution {
public:
    bool isVowel(char s) {
        if (s == 'a' || s == 'e' || s == 'i' || s == 'o' || s == 'u' || s == 'A' || s == 'E' || s == 'I' || s == 'O' || s == 'U')
            return true;
        else
            return false;
    }
    string reverseVowels(string s) {
        if (s.size() == 0)
            return "";
        int l = 0, r = s.size() - 1;
        if (!isVowel(s[l]))
            l++;
        if (!isVowel(s[r]))
            r--;
        while (l < r) {
            if (isVowel(s[l]) && isVowel(s[r]))
                swap(s[l++], s[r--]);
            if (!isVowel(s[l]))
                l++;
            if (!isVowel(s[r]))
                r--;
        }
        return s;
    }
};

//Created by bryantbyr on 20170831
//Time:O(n)
//Space:O(1)
//Two Pointers (be better)
class Solution {
public:
    bool isVowel(char s) {
        if (s == 'a' || s == 'e' || s == 'i' || s == 'o' || s == 'u' || s == 'A' || s == 'E' || s == 'I' || s == 'O' || s == 'U')
            return true;
        else
            return false;
    }
    string reverseVowels(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (!isVowel(s[l]))
                l++;
            if (!isVowel(s[r]))
                r--;
            if (l < r && isVowel(s[l]) && isVowel(s[r]))
                swap(s[l++], s[r--]);
        }
        return s;
    }
};

//Learn from discuss on 20170831
//Time:O(n)
//Space:O(1)
//Two Pointers
class Solution {
public:
    string reverseVowels(string s) {
        int dict[256] = {0};//use array to check if a letteer is a vowel
        dict['a'] = 1, dict['A'] = 1;
        dict['e'] = 1, dict['E'] = 1;
        dict['i'] = 1, dict['I'] = 1;
        dict['o'] = 1, dict['O'] = 1;
        dict['u'] = 1, dict['U'] = 1;
        int l = 0, r = s.size() - 1;
        // cout<<s[-1]<<endl; //s[-1] is ""
        if (dict[(int)s[l]] == 0)
            l++;
        if (dict[(int)s[r]] == 0)
            r--;
        while (l < r) {
            if (dict[(int)s[l]] == 1 && dict[(int)s[r]] == 1)
                swap(s[l++], s[r--]);
            if (dict[(int)s[l]] == 0)
                l++;
            if (dict[(int)s[r]] == 0)
                r--;
        }
        return s;
    }
};

//Learn from discuss on 20170831
//Time:O(n)
//Space:O(1)
//Two Pointers + string
class Solution {
public:
    string reverseVowels(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j) {
            i = s.find_first_of("aeiouAEIOU", i);
            j = s.find_last_of("aeiouAEIOU", j);
            if (i < j) {
                swap(s[i++], s[j--]);
            }
        }
        return s;
    }
};

int main()
{
    Solution s;
    string t = "leetcode";
    t = s.reverseVowels(t);
    cout << t << endl;
}
