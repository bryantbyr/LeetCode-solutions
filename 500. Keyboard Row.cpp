//500. Keyboard Row.cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;

//Created by bryantbyr on 20171005
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        unordered_set<char> set1 = {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'};
        unordered_set<char> set2 = {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'};
        unordered_set<char> set3 = {'Z', 'X', 'C', 'V', 'B', 'N', 'M'};
        vector<string> res;
        for (unsigned i = 0; i < words.size(); ++i) {
            int a = 0, b = 0, c = 0;
            for (int j = 0; j < words[i].size(); ++j) {
                if (set1.find(toupper(words[i][j])) != set1.end())
                    a++;
                else if (set2.find(toupper(words[i][j])) != set2.end())
                    b++;
                else
                    c++;
            }
            if (a == words[i].size() || b == words[i].size() || c == words[i].size())
                res.push_back(words[i]);
        }
        return res;
    }
};

//Learn from discuss on 20171005
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<string> s = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        unordered_map<char, int> map;
        for (unsigned i = 0; i < s.size(); ++i) {
            for (auto c : s[i])
                map[c] = i;
        }
        vector<string> res;
        for (auto word : words) {
            int index = 0;
            if (word.size() > 0)
                index = map[tolower(word[0])];
            for (unsigned i = 1; i < word.size(); ++i) {
                if (index != map[tolower(word[i])]) {
                    index = -1;
                    break;
                }
            }
            if (index != -1)
                res.push_back(word);
        }
        return res;
    }
};

int main()
{
    Solution S;
    vector<string> v = {"Hello", "Alaska", "Dad", "Peace"};
    vector<string> r = S.findWords(v);
    for (unsigned i = 0; i < r.size(); ++i) {
        cout << r[i] << endl;
    }
}
