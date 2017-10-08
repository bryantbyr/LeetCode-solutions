//447. Number of Boomerangs.cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <math.h>
using namespace std;

//Created by bryantbyr on 20171008
//Time:O(n^2)
//Space:O(n)
//Hash Table
class Solution {
public:
    int numberOfBoomerangs(vector<pair<int, int>>& points) {
        int res = 0;
        for (unsigned i = 0; i < points.size(); ++i) {
            unordered_map<int, int> map;
            for (unsigned j = 0; j < points.size(); ++j) {
                int dis = (points[i].first - points[j].first) * (points[i].first - points[j].first)
                          + (points[i].second - points[j].second) * (points[i].second - points[j].second);
                map[dis] ++;
            }
            // for (auto it = map.begin(); it != map.end(); ++it)
            //     res += it->second == 1 ? 0 : it->second * (it->second - 1);
            for (auto& p : map)
                res += p.second * (p.second - 1);
        }
        return res;
    }
};

//Learn from discuss on 20171008
//Time:O(n*n*log(n))
//Space:O(n)
//Sort
class Solution {
public:
    int numberOfBoomerangs(vector<pair<int, int>>& points) {
        int cnt = 0, n = points.size();
        int dis[n];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int x = points[i].first - points[j].first;
                int y = points[i].second - points[j].second;
                dis[j] = x * x + y * y;
            }
            sort(dis, dis + n);
            int k = 1;
            for (int j = 1; j < n; ++j) {
                if (dis[j] == dis[j - 1])
                    ++k;
                else {
                    cnt += k * (k - 1);
                    k = 1;
                }
            }
            cnt += k * (k - 1);
        }
        return cnt;
    }
};

//Learn from discuss on 20171008
//Time:O(n^2)
//Space:O(n)
//Hash Table
class Solution {
public:
    int numberOfBoomerangs(vector<pair<int, int>>& points) {
        int res = 0;
        for (auto &p : points) {
            unordered_map<int, int> ctr(points.size());
            for (auto &q : points)
                res += 2 * ctr[pow(p.first - q.first, 2) + pow(p.second - q.second, 2)]++;
        }
        return res;
    }
};

int main()
{
    Solution S;
    vector<pair<int, int>> points = {{0, 0}, {1, 0}, { -1, 0}, {0, 1}, {0, -1}};
    cout << S.numberOfBoomerangs(points) << endl;
}
