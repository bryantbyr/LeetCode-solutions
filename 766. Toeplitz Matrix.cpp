//766. Toeplitz Matrix.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20180221
//Time:O(m*n)
//Space:O(1)
//Array
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        for (int i = 0; i < m; ++i) {
            int j = i + 1, k = 1;
            while (j < m && k < n) {
                if (matrix[j][k] != matrix[j - 1][k - 1])
                    return false;
                j++;
                k++;
            }
        }
        for (int i = 1; i < n; ++i) {
            int j = 1, k = i + 1;
            while (k < n && j < m) {
                if (matrix[j][k] != matrix[j - 1][k - 1])
                    return false;
                j++;
                k++;
            }
        }
        return true;
    }
};

int main()
{
    Solution s;
    vector<vector<int>> v = {{1, 2, 3, 4}, {5, 1, 2, 3}, {9, 5, 1, 2}};
    cout << s.isToeplitzMatrix(v) << endl;
    return 0;
}
