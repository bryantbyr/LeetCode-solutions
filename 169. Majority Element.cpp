//169. Majority Element.cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

//Created by bryantbyr on 20170919
//Time:O(nlog(n))
//Space:O(1)
//array
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // if(nums.size()==0)
        //     return -1;
        sort(nums.begin(), nums.end());
        int count = 1;
        for (unsigned i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] == nums[i + 1])
                count++;
            else
                count = 1;
            if (count > (int)nums.size() / 2)
                return nums[i];
        }
        return nums[0];
    }
};

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

//Created by bryantbyr on 21070920
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> map;
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (++map[nums[i]] > (int)nums.size() / 2)
                return nums[i];
        }
    }
};

//Learn from discuss on 20170920
//Time:O(n)
//Space:O(1)
//Moore's voting algorithm
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major = nums[0], count = 1;
        for (unsigned i = 1; i < nums.size(); ++i) {
            if (nums[i] == major)
                count++;
            else
                count--;
            if (count == 0) {
                count = 1;
                major = nums[i];
            }
        }
        return major;
    }
};

//Learn from discuss on 20170920
//Time:O(nlog(n))
//Space:O(1)
//Divide and Conquer
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        return helper(nums, 0, nums.size() - 1);
    }
private:
    int helper(vector<int>& nums, int left, int right) {
        if (left == right)
            return nums[left];
        int mid = left + (right - left) / 2;
        int lm = helper(nums, left, mid);
        int rm = helper(nums, mid + 1, right);
        if (lm == rm)
            return lm;
        // if (count(nums.begin() + left, nums.begin() + right + 1, lm) > count(count(nums.begin() + left, nums.begin() + right + 1, rm)))
        //     return lm;
        // else
        //     return rm;
        return count(nums.begin() + left, nums.begin() + right + 1, lm) > count(nums.begin() + left, nums.begin() + right + 1, rm) ? lm : rm;
    }
};

int main()
{
    Solution S;
    vector<int> v = {1, 3, 3, 2, 2, 4, 2, 3, 3};
    cout << S.majorityElement(v) << endl;
}
