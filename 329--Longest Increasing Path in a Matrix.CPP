//329--Longest Increasing Path in a Matrix.CPP

#include <iostream>
#include <vector>
using namespace std;

//20170531
//DFS+记忆化搜索
class Solution {
private:
    vector<vector<int>> cache;
    vector<pair<int, int>> direction;
    int DFS(int i, int j, vector<vector<int>>& matrix)
    {
        if (cache[i][j] != 0)
            return cache[i][j];
        int res = 1;
        for (auto dir : direction) {
            int x = i + dir.first, y = j + dir.second;
            if (x < 0 || y < 0 || x >= matrix.size() || y >= matrix[0].size() || matrix[i][j] >= matrix[x][y])
                continue;
            else
                res = max(res, DFS(x, y, matrix) + 1);
        }
        return cache[i][j] = res;
    }
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty())
            return 0;
        cache = vector<vector<int>>(matrix.size(), vector<int>(matrix[0].size(), 0));
        direction.push_back(pair<int, int>(0, -1));
        direction.push_back(pair<int, int>(0, 1));
        direction.push_back(pair<int, int>(-1, 0));
        direction.push_back(pair<int, int>(1, 0));
        int res = 1;
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                res = max(res, DFS(i, j, matrix));
            }
        }
        return res;
    }
};


int main()
{
    Solution s;
    vector<vector<int>> v;
    int n;
    cin >> n;
    int m;
    cin>>m;
    vector<int> temp(m, 0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            cin >> temp[j];
        v.push_back(temp);
    }
    // for(auto i:v){
    //     for(auto j:i)
    //         cout<<j<<" ";
    //     cout<<endl;
    // }
    cout << s.longestIncreasingPath(v) << endl;

}
