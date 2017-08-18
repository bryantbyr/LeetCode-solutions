//62. Unique Paths.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170818
//Time:O(m+n) | O(m*n)
//Space:O(1) | O(m*n)
//组合数 | DP
class Solution {
public:
    int uniquePaths(int m, int n) {
        /*
        方法一:组合数
         */
        // unsigned long long r = 1;
        // int i = m, j = 1;
        // while (i <= n + m - 2 || j < n - 1) {
        //     if (i <= n + m - 2) {
        //         r *= i;
        //         i++;
        //     }
        //     if (j < n - 1 && r % j == 0) {
        //         r /= j;
        //         j++;
        //     }
        // }
        // return r;

        /*
        方法二:DP(递推)
         */
        if (m * n == 0)
            return 0;
        vector<vector<int>> dp(m, vector<int>(n, 1));
        for (int i = 1; i < m; ++i)
            for (int j = 1; j < n; ++j)
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        return dp[m - 1][n - 1];
    }
};

int main()
{
    Solution s;
    cout << s.uniquePaths(23, 12) << endl;
}
