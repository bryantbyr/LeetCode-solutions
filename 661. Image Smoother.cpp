//661. Image Smoother.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170926
//Time:O(n*m)
//Space:O(n*m)
//array
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        if (M.size() == 0 || M[0].size() == 0)
            return M;
        int n = M.size();
        int m = M[0].size();
        vector<vector<int>> r(n, vector<int>(m));
        if (n == 1) {
            if (m == 1)
                return M;
            else {
                r[0][0] = (M[0][0] + M[0][1]) / 2;
                for (unsigned i = 1; i < m - 1; ++i) {
                    r[0][i] = (M[0][i - 1] + M[0][i] + M[0][i + 1]) / 3;
                }
                r[0][m - 1] = (M[0][m - 1] + M[0][m - 2]) / 2;
                return r;
            }
        }
        if (m == 1) {
            if (n == 1)
                return M;
            else {
                r[0][0] = (M[0][0] + M[1][0]) / 2;
                for (unsigned i = 1; i < n - 1; ++i) {
                    r[i][0] = (M[i - 1][0] + M[i][0] + M[i + 1][0]) / 3;
                }
                r[n - 1][0] = (M[n - 2][0] + M[n - 1][0]) / 2;
                return r;
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (i == 0) {
                    if (j != 0 && j != m - 1)
                        r[i][j] = (M[i][j - 1] + M[i][j] + M[i][j + 1] + M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]) / 6;
                    else if (j == 0)
                        r[0][0] = (M[0][0] + M[0][1] + M[1][0] + M[1][1]) / 4;
                    else
                        r[0][m - 1] = (M[0][m - 1] + M[0][m - 2] + M[1][m - 1] + M[1][m - 2]) / 4;
                }
                else if (i == n - 1) {
                    if (j != 0 && j != m - 1)
                        r[i][j] = (M[i][j - 1] + M[i][j] + M[i][j + 1] + M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1]) / 6;
                    else if (j == 0)
                        r[n - 1][0] = (M[n - 1][0] + M[n - 1][1] + M[n - 2][0] + M[n - 2][1]) / 4;
                    else
                        r[n - 1][m - 1] = (M[n - 1][m - 1] + M[n - 1][m - 2] + M[n - 2][m - 1] + M[n - 2][m - 2]) / 4;
                }
                else {
                    if (j == 0)
                        r[i][j] = (M[i][j + 1] + M[i][j] + M[i - 1][j] + M[i - 1][j + 1] + M[i + 1][j] + M[i + 1][j + 1]) / 6;
                    else if (j == m - 1)
                        r[i][j] = (M[i][j - 1] + M[i][j] + M[i - 1][j] + M[i - 1][j - 1] + M[i + 1][j] + M[i + 1][j - 1]) / 6;
                    else
                        r[i][j] = (M[i][j - 1] + M[i][j] + M[i][j + 1] + M[i - 1][j] + M[i - 1][j - 1] + M[i - 1][j + 1] + M[i + 1][j] + M[i + 1][j - 1] + M[i + 1][j + 1]) / 9;
                }
            }
        }
        return r;
    }
};

//Learn from discuss on 20170927
//Time:O(n*m)
//Space:O(n*m)
//array
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        vector<vector<int>> res = M;
        int m = M.size();
        int n = (m ? M[0].size() : 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                res[i][j] = smooth (M, i, j, m, n);
            }
        }
        return res;
    }
    int smooth (vector<vector<int>>& M, int i, int j, int m, int n) {
        int cnt = 1;
        int avg = M[i][j];
        if (j - 1 >= 0) {
            avg += M[i][j - 1];
            ++cnt;
        }
        if (j + 1 < n) {
            avg += M[i][j + 1];
            ++cnt;
        }
        if (i - 1 >= 0) {
            avg += M[i - 1][j];
            ++cnt;
            if (j - 1 >= 0) {
                avg += M[i - 1][j - 1];
                ++cnt;
            }
            if (j + 1 < n) {
                avg += M[i - 1][j + 1];
                ++cnt;
            }
        }
        if (i + 1 < m) {
            avg += M[i + 1][j];
            ++cnt;
            if (j - 1 >= 0) {
                avg += M[i + 1][j - 1];
                ++cnt;
            }
            if (j + 1 < n) {
                avg += M[i + 1][j + 1];
                ++cnt;
            }
        }
        return avg / cnt;
    }
};

//Learn from discuss on 20170927
//Time:O(n*m)
//Space:O(n*m)
//array
class Solution {
private:
    bool valid(int i, int j, vector<vector<int>>& M)
    {
        return i >= 0 && i < M.size() && j >= 0 && j < M[0].size();
    }

public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        vector<vector<int>> res;
        if (M.size() == 0 || M[0].size() == 0)
            return res;
        for (int i = 0; i < M.size(); i++)
        {
            vector<int> cur;
            for (int j = 0; j < M[0].size(); j++)
            {
                int total = 0;
                int count = 0;
                for (int x = -1; x < 2; x++)
                {
                    for (int y = -1; y < 2; y++)
                    {
                        if (valid(i + x, j + y, M))
                        {
                            count++;
                            total += M[i + x][j + y];
                        }
                    }
                }
                cur.push_back(total / count);
            }
            res.push_back(cur);
        }
        return res;
    }
};

int main()
{
    Solution S;
    // vector<vector<int>> v = {{2, 3, 4}, {5, 6, 7}, {8, 9, 10},{11,12,13},{14,15,16}};
    vector<vector<int>> v = {{3}, {2}};
    vector<vector<int>> r = S.imageSmoother(v);
    for (unsigned i = 0; i < r.size(); ++i) {
        for (unsigned j = 0; j < r[0].size(); ++j)
            cout << r[i][j] << "    ";
        cout << endl;
    }
}
