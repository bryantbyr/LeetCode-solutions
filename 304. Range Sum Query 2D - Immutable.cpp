//304. Range Sum Query 2D - Immutable.cpp
#include <iostream>
#include <vector>
using namespace std;


//Created by bryantbyr on 20170818
//Time:O(n^2)
//Soace:O(n^2)
//DP
class NumMatrix {
public:
    NumMatrix(vector<vector<int>> matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            dp = {};//可省去
            return;
        }
        vector<int> t;
        for (unsigned int i = 0; i <= matrix.size(); ++i)
        {
            t.push_back(0);
            for (unsigned int j = 1; j <= matrix[0].size(); ++j)
            {
                if (i != 0)//back()函数访问vector最后一个元素
                    t.push_back(t.back() + matrix[i - 1][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]);
                else
                    t.push_back(0);
            }
            dp.push_back(t);
            t.clear();
        }
    }
    int sumRegion(int row1, int col1, int row2, int col2) {
        if (0 <= row1 && row2 < dp.size() && 0 <= col1 && col2 < dp[0].size())
            return dp[row2 + 1][col2 + 1] - dp[row1][col2 + 1] - dp[row2 + 1][col1] + dp[row1][col1];
        //cout<<"test"<<endl; //注意此种情况的返回值,后面有执行其他语句时返回值不确定,没有时返回0
        // else
        //     return 0;
    }
private:
    vector<vector<int>> dp;
};


int main()
{
    // vector<vector<int>> m = {
    //     {3, 0, 1, 4, 2},
    //     {5, 6, 3, 2, 1},
    //     {1, 2, 0, 1, 5},
    //     {4, 1, 0, 1, 7},
    //     {1, 0, 3, 0, 5}
    // };
    vector<vector<int>> m = {{}};
    NumMatrix* obj = new NumMatrix(m);
    cout << obj->sumRegion(0, 0, 0, 0) << endl;
}
