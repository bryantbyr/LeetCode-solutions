//169. Majority Element.cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//Created by bryantbyr on 20170919
//Time:O(nlog(n))
//Space:O(1)
//array
// class Solution {
// public:
//     int majorityElement(vector<int>& nums) {
//         // if(nums.size()==0)
//         //     return -1;
//         sort(nums.begin(), nums.end());
//         int count = 1;
//         for (unsigned i = 0; i < nums.size() - 1; ++i) {
//             if (nums[i] == nums[i + 1])
//                 count++;
//             else
//                 count = 1;
//             if (count > (int)nums.size() / 2)
//                 return nums[i];
//         }
//         return nums[0];
//     }
// };

//Learn from discuss on 20170919
//Time:O(nlog(n))
//Space:O(1)
//array
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums[nums.size() / 2];
    }
};

int main()
{
    Solution S;
    vector<int> v = {1};
    cout << S.majorityElement(v) << endl;
}
