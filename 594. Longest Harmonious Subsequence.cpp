//594. Longest Harmonious Subsequence.cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

//Created by bryantbyr on 20171009
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    int findLHS(vector<int>& nums) {
        map<int, int> map;
        for (unsigned i = 0; i < nums.size(); ++i)
            map[nums[i]]++;
        int res = 0;
        bool start = true;
        int lastKey = 0;
        int lastValue = 0;
        for (auto& m : map) {
            if (start)
                start = false;
            else if (m.first - lastKey == 1)
                res = max(m.second + lastValue, res);
            lastKey = m.first;
            lastValue = m.second;
        }
        return res;
    }
};

//Created by bryantbyr on 20171009
//Time:O(n*log(n))
//Space:O(1)
//Sort
class Solution {
public:
    int findLHS(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int res = 0;
        int last = 0;
        int cur = 1;
        int flag = false;
        for (unsigned i = 1; i < nums.size(); ++i) {
            if (flag)
                res = max(last + cur, res);
            if (nums[i] == nums[i - 1])
                cur++;
            else if (nums[i] - nums[i - 1] == 1) {
                flag = true;
                last = cur;
                cur = 1;
            }
            else {
                flag = false;
                cur = 1;
            }
        }
        if (flag)
            res = max(last + cur, res);
        return res;
    }
};

//Learn from discuss on 20171009
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    int findLHS(vector<int>& nums) {
        map<int, int> map;
        for (unsigned i = 0; i < nums.size(); ++i)
            map[nums[i]]++;
        int res = 0;
        for (auto& m : map) {
            if (map.find(m.first + 1) != map.end())
                res = max(map[m.first + 1] + m.second, res);
        }
        return res;
    }
};

int main()
{
    Solution S;
    vector<int> v = {};
    cout << S.findLHS(v) << endl;
}
