//118. Pascal's Triangle.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170927
//Time:O(n^2)
//Space:O(n^2)
//array
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> r;
        for (int i = 0; i < numRows; ++i) {
            vector<int> t(i + 1, 0);
            t[0] = t[i] = 1;
            for (int j = 1; j < i; ++j)
                t[j] = r[i - 1][j - 1] + r[i - 1][j];
            r.push_back(t);
        }
        return r;
    }
};

//Learn from discuss on 20170927
//Time:O(n^2)
//Space:O(n^2)
//array
class Solution {
public:
    vector<vector<int>> generate(int n) {
        vector<vector<int> > res;
        vector<int> tmp;
        for (int i = 0; i < n; i++) {
            if (res.empty())
                tmp.push_back(1);
            else {
                int last = 0;
                for (int j = 0; j < res.back().size(); j++) {
                    tmp.push_back(last + res.back()[j]);
                    last = res.back()[j];
                }
                tmp.push_back(1);
            }
            res.push_back(tmp);
            tmp.clear();
        }
        return res;
    }
};

//Learn from discuss on 20170927
//Time:O(n^2)
//Space:O(n^2)
//array
class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int>> r(numRows);
        for (int i = 0; i < numRows; i++) {
            r[i].resize(i + 1);
            r[i][0] = r[i][i] = 1;
            for (int j = 1; j < i; j++)
                r[i][j] = r[i - 1][j - 1] + r[i - 1][j];
        }
        return r;
    }
};

int main()
{
    Solution S;
    vector<vector<int>> r = S.generate(5);
    for (unsigned i = 0; i < r.size(); ++i) {
        for (unsigned j = 0; j < r[i].size(); ++j) {
            cout << r[i][j] << "  ";
        }
        cout << endl;
    }
}
