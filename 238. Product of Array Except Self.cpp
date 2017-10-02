//238. Product of Array Except Self.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20171002
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(), 0);
        for (int i = nums.size() - 1; i >= 0; --i)
            res[i] = (i == nums.size() - 1) ? nums[i] : res[i + 1] * nums[i];
        int temp = 1;
        for (unsigned i = 0; i < nums.size(); ++i) {
            res[i] = (i == nums.size() - 1) ? temp : temp * res[i + 1];
            temp *= nums[i];
        }
        return res;
    }
};

//Learn from discuss on 20171002
//Time:O(n)
//Space:O(1)
//array*
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int fromBegin = 1;
        int fromLast = 1;
        vector<int> res(n, 1);
        for (int i = 0; i < n; i++) {
            res[i] *= fromBegin;
            fromBegin *= nums[i];
            res[n - 1 - i] *= fromLast;
            fromLast *= nums[n - 1 - i];
        }
        return res;
    }
};

int main()
{
    Solution S;
    vector<int> v = {1, 2, 3, 4};
    vector<int> r = S.productExceptSelf(v);
    for (unsigned i = 0; i < r.size(); ++i)
        cout << r[i] << endl;

}
