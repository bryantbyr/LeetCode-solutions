/*53. Maximum Subarray.cpp*/
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170817
//Time:O(n)
//Space:O(1)
//DP+"灵感"
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int r = -INT_MAX;//注意r的取值
        int sum = 0;
        for (unsigned int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            if (sum > r)//注意比较语句的位置
                r = sum;
            if (sum < 0)
                sum = 0;
            // if (sum > 0)
            //     sum += nums[i];
            // else
            //     sum = nums[i];
            // if (sum > r)
            //     r = sum;
        }
        return r;
    }
};

int main()
{
    Solution s;
    vector<int> nums = { -2};
    cout << s.maxSubArray(nums) << endl;
}

