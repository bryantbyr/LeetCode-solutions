//643. Maximum Average Subarray I.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170925
//Time:O(n)
//Space:O(1)
//array + Sliding Window
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double t = 0, r = INT_MIN;
        for (unsigned i = 0; i < nums.size(); ++i) {
            t += nums[i];
            if (i >= k)
                t -= nums[i - k];
            if (i >= k - 1)
                r = max(t, r);
        }
        return r / k;
    }
};

//Learn from discuss on 20170925
//Time:O(n)
//Space:O(1)
//Sliding Window
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double t = 0;
        for (unsigned i = 0; i < k; ++i)
            t += nums[i];
        double r = t;
        for (unsigned i = k; i < nums.size(); ++i) {
            t += nums[i] - nums[i - k];
            r = max(t, r);
        }
        return r / k;
    }
};

int main()
{
    Solution S;
    vector<int> v = {1, 12, -5, -6, 50, 3};
    cout << S.findMaxAverage(v, 4) << endl;
}
