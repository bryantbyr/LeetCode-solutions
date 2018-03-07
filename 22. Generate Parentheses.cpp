//22. Generate Parentheses.cpp
#include <iostream>
#include <vector>
using namespace std;

//Learn from discuss on 20180307
//Time: < O(2^n)
//Space:O(1)
//Backtrack + string
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        backtrack(res, "", 0, 0, n);
        return res;
    }
    void backtrack(vector<string>& res, string s, int left, int right, int n) {
        if ((int)s.size() == n * 2) {
            res.push_back(s);
            return;
        }
        if (left < n)
            backtrack(res, s + '(', left + 1, right, n);
        if (right < left)
            backtrack(res, s + ')', left, right + 1, n);
    }
};

int main()
{
    Solution S;
    vector<string> r = S.generateParenthesis(3);
    for (unsigned i = 0; i < r.size(); ++i) {
        cout << r[i] << endl;
    }
}
