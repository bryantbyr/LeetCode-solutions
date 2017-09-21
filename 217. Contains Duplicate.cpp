//217. Contains Duplicate.cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <set>
using namespace std;

//Created by bryantbyr on 20170921
//Time:O(n^2)
//Space:O(1)
//Brute Force (Time Limit Exceeded)
// class Solution {
// public:
//     bool containsDuplicate(vector<int>& nums) {
//         for (unsigned i = 0; i < nums.size(); ++i) {
//             for (unsigned j = i + 1; j < nums.size(); ++j) {
//                 if (nums[j] == nums[i])
//                     return true;
//             }
//         }
//         return false;
//     }
// };

//Created by bryantbyr on 20170921
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> map;
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (++map[nums[i]] > 1)
                return true;
        }
        return false;
    }
};

//Created by bryantbyr on 20170921
//Time:O(n)
//Space:O(n)
//set
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set;
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (set.find(nums[i]) != set.end())
                return true;
            set.insert(nums[i]);
        }
        return false;
    }
};

//Created by bryantbyr on 20170921
//Time:O(nlog(n))
//Space:O(1)
//sort
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (unsigned i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1])
                return true;
        }
        return false;
    }
};

//Learn from discuss on 20170921
//Time:O(n)
//Space:O(n)
//unordered_set
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        //return nums.size() > set<int>(nums.begin(), nums.end()).size();
        return nums.size() > unordered_set<int>(nums.begin(), nums.end()).size();
    }
};

int main()
{
    Solution S;
    vector<int> v = {2, 5, 6, 1, 2, 9};
    cout << S.containsDuplicate(v) << endl;
}
