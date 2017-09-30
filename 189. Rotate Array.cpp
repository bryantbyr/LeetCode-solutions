//189. Rotate Array.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by brynatbyr on 20170930
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.size() == 0)
            return;
        int step = k % nums.size();
        for (int i = 0; i < step; ++i)
        {
            int temp = nums[nums.size() - 1];
            for (unsigned i = nums.size() - 1; i > 0; --i)
                nums[i] = nums[i - 1];
            nums[0] = temp;
        }
    }
};

//Created by brynatbyr on 20170930
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.size() == 0)
            return;
        int step = k % nums.size();
        vector<int> temp(step, 0);
        for (int i = 0; i < step; ++i)
            temp[i] = nums[nums.size() - step + i];
        for (int i = (int)nums.size() - 1; i >= 0 ; --i)// unsigned >=0 != int >= 0
        {
            if (i < step)
                nums[i] = temp[i];
            else
                nums[i] = nums[i - step];
        }
    }
};

//Created by brynatbyr on 20170930
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.size() == 0)
            return;
        int step = k % nums.size();
        nums.insert(nums.end(), step, 0);
        for (int i = (int)nums.size() - 1; i >= 0 ; --i)
            nums[i] = i >= step ? nums[i - step] : nums[nums.size() + i - step];
        nums.assign(nums.begin(), nums.end() - step);
    }
};

//Learn from discuss on 20170930
//Time:O(n)
//Space:O(n)
//array
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> temp(nums.size(), 0);
        for (int i = 0; i < nums.size(); i++)
            temp[(i + k) % nums.size()] = nums[i];
        for (int i = 0; i < nums.size(); i++)
            nums[i] = temp[i];
    }
};

//Learn from discuss on 20170930
//Time:O(n)
//Space:O(1)
//array
class Solution
{
public:
    void rotate(vector<int>& nums, int k) {
        k = k % nums.size();
        reverse(nums.begin(), nums.begin() + nums.size() - k);
        reverse(nums.begin() + nums.size() - k, nums.begin() + nums.size());
        reverse(nums.begin(), nums.begin() + nums.size());
    }
};

int main()
{
    Solution S;
    vector<int> v = {1, 2, 3, 4, 5, 6, 7};
    S.rotate(v, 3);
    for (unsigned i = 0; i < v.size(); ++i) {
        cout << v[i] << "  ";
    }
}
