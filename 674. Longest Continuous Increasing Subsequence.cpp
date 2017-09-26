//674. Longest Continuous Increasing Subsequence.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170926
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        int t = 1, r = 1;
        for (unsigned i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i - 1])
                t++;
            else {
                r = max(t, r);
                t = 1;
            }
        }
        r = max(t, r);
        return r;
    }
};

//Created by bryantbyr on 20170926
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        int t = 1, r = 1;
        for (unsigned i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i - 1])
                r = max(++t, r);
            else
                t = 1;
        }
        return r;
    }
};

//Created by bryantbyr on 20170926
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int t = 0, r = 0;
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (i == 0 || nums[i] > nums[i - 1])
                r = max(++t, r);
            else
                t = 1;
        }
        return r;
    }
};

//Learn from on 20170926
//Time:O(n)
//Space:O(1)
//array + Two Pointers
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int r = 0;
        for (int i = 0, j = 0; i < (int)nums.size(); ++i) {
            if (i == 0 || nums[i] <= nums[i - 1])
                j = i;
            r = max(r, i - j + 1);
        }
        return r;
    }
};



int main()
{
    Solution S;
    vector<int> v = {2, 2, 2, 2};
    cout << S.findLengthOfLCIS(v) << endl;
}
