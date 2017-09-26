//566. Reshape the Matrix.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170926
//Time:O(n*m)
//Space:O(n*m)
//array
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        if (nums.size() == 0 || nums[0].size() == 0)
            return nums;
        int m = nums.size(), n = nums[0].size();
        if (m * n != r * c)
            return nums;
        vector<vector<int>> result(r, vector<int>(c));
        int rIndex = 0, cIndex = 0;
        for (unsigned i = 0; i < r; ++i) {
            for (unsigned j = 0; j < c; ++j) {
                result[i][j] = nums[rIndex][cIndex++];
                if (cIndex == n) {
                    rIndex++;
                    cIndex = 0;
                }
            }
        }
        return result;
    }
};

//Learn from discuss on 20170926
//Time:O(n*m)
//Space:O(n*m)
//array
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int m = nums.size(), n = nums[0].size();
        if (m * n != r * c)
            return nums;
        vector<vector<int>> result(r, vector<int>(c));
        for (unsigned i = 0; i < r * c; ++i)
            result[i / c][i % c] = nums[i / n][i % n];
        return result;
    }
};

int main()
{
    Solution S;
    vector<vector<int>> v = {{1, 2}, {3, 4}};
    vector<vector<int>> r = S.matrixReshape(v, 1, 4);
    for (unsigned i = 0; i < r.size(); ++i) {
        for (unsigned j = 0; j < r[0].size(); ++j)
            cout << r[i][j] << "  ";
        cout << endl;
    }
}
