//463. Island Perimeter.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20171006
//Time:O(n^2)
//Space:O(1)
//Hash Table
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int res = 0;
        for (unsigned i = 0; i < grid.size(); ++i) {
            for (unsigned j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) {
                    if (i == 0 || grid[i - 1][j] == 0)
                        res++;
                    if (i == grid.size() - 1 || grid[i + 1][j] == 0)
                        res++;
                    if (j == 0 || grid[i][j - 1] == 0)
                        res++;
                    if (j == grid[0].size() - 1 || grid[i][j + 1] == 0)
                        res++;
                }
            }
        }
        return res;
    }
};

//Learn from discuss on 20171006
//Time:O(n^2)
//Space:O(1)
//Hash Table
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int island = 0, repeat = 0;
        for (unsigned i = 0; i < grid.size(); ++i) {
            for (unsigned j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) {
                    island++;
                    if (i != 0 && grid[i - 1][j] == 1)
                        repeat++;
                    if (j != 0 && grid[i][j - 1] == 1)
                        repeat++;
                }
            }
        }
        return island * 4 - repeat * 2;
    }
};

int main()
{
    Solution S;
    vector<vector<int>> v = {{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {1, 1, 0, 0}};
    cout << S.islandPerimeter(v) << endl;
}
