#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

//Created by bryantbyr on 20170222
//Time:O(n^2)
//Space:O(1)
//Brute Force
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        vector<int> s;
        int k = 0;
        for (int i = 0; i < (int)nums.size(); ++i)
        {
            for (int j = i + 1; j < (int)nums.size(); ++i)
            {
                if ((nums[i] + nums[j]) == target)
                {
                    s.push_back(i);
                    s.push_back(j);
                    k = 1;
                    break;
                }
            }
            if (k == 1)
                break;
        }
        return s;
    }
};

//Created by bryantbyr on 20170914
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> r = {};
        unordered_map<int, int> map;
        for (unsigned i = 0; i < nums.size(); ++i)
            map[nums[i]] = i;
        for (unsigned i = 0; i < nums.size(); i++) {
            if (map.find(target - nums[i]) != map.end()) {
                r.push_back(map[target - nums[i]]);
                r.push_back(i);
                break;
            }
            //map[nums[i]] = i;
        }
        return r;
    }
};

//Created by bryantbyr on 20170914
//Time:O(n)
//Space:O(n)
//Two Pointers (to be improved!)
// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         vector<int> r = {};
//         sort(nums.begin(), nums.end());
//         int start = 0, end = nums.size() - 1;
//         while (start < end) {
//             if (nums[start] + nums[end] < target)
//                 start++;
//             else if (nums[start] + nums[end] > target)
//                 end--;
//             else {
//                 r.push_back(start);
//                 r.push_back(end);
//                 break;
//             }
//         }
//         return r;
//     }
// };

int main()
{
    Solution S;
    vector<int> v = {3, 3};
    int target = 6;
    vector<int> r = S.twoSum(v, target);
    for (unsigned i = 0; i < r.size(); ++i)
        cout << r[i] << endl;
    return 0;
}
