//628. Maximum Product of Three Numbers.cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//Learn from discuss on 20170922
//Time:O(nlog(n))
//Space:O(1)
//array
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int t1 = nums[nums.size() - 1] * nums[nums.size() - 2] * nums[nums.size() - 3];
        int t2 = nums[0] * nums[1] * nums[nums.size() - 1];
        return max(t1, t2);
    }
};


int main()
{
    Solution S;
    vector<int> v = {1, 3, 2, 4};
    cout << S.maximumProduct(v) << endl;
}
