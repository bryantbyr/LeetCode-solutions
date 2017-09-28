//119. Pascal's Triangle II.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170928
//Time:O(n^2)
//Space:O(n)
//array
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res(rowIndex + 1, 0);
        res[0] = 1;
        for (int i = 1; i <= rowIndex; ++i) {
            for (int j = i; j >= 1; --j)
                res[j] += res[j - 1];
        }
        return res;
    }
};

int main()
{
    Solution S;
    vector<int> res = S.getRow(3);
    for (unsigned i = 0; i < res.size(); ++i) {
        cout << res[i] << "  ";
    }
}
