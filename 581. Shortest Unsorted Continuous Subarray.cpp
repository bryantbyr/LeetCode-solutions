//581. Shortest Unsorted Continuous Subarray.cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//Created by bryantbyr on 20170925
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        if (is_sorted(nums.begin(), nums.end()))
            return 0;
        int start = 0, end = nums.size() - 1;
        for (unsigned i = 1; i < nums.size(); ++i) {
            if (nums[i] >= nums[i - 1])
                start = i;
            else
                break;
        }
        for (unsigned i = nums.size() - 2; i >= 0; --i) {
            if (nums[i] <= nums[i + 1])
                end = i;
            else
                break;
        }
        while (start != 0 && *min_element(nums.begin() + start, nums.begin() + end + 1) < nums[start - 1])
            start--;
        while (end != nums.size() - 1 && *max_element(nums.begin() + start, nums.begin() + end + 1) > nums[end + 1])
            end++;
        return end - start + 1;
    }
};

//Created by bryantbyr on 20170925
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        if (is_sorted(nums.begin(), nums.end()))
            return 0;
        int start = 0, end = nums.size() - 1;
        for (unsigned i = 1; i < nums.size() && nums[i] >= nums[i - 1]; ++i)
            start = i;
        for (unsigned i = nums.size() - 2; i >= 0 && nums[i] <= nums[i + 1]; --i)
            end = i;
        while (start != 0 && *min_element(nums.begin() + start, nums.begin() + end + 1) < nums[start - 1])
            start--;
        while (end != nums.size() - 1 && *max_element(nums.begin() + start, nums.begin() + end + 1) > nums[end + 1])
            end++;
        return end - start + 1;
    }
};

//Learn from discuss on 20170928
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int start = 0, end = 1, Max = nums[0], Min = nums[nums.size() - 1];
        for (unsigned i = 1; i < nums.size(); ++i) {
            Max = max(Max, nums[i]);
            Min = min(Min, nums[nums.size() - i - 1]);
            if (Max > nums[i])
                start = i;
            if (Min < nums[nums.size() - i - 1])
                end = nums.size() - i - 1;
        }
        return start - end + 1;
    }
};


int main()
{
    Solution S;
    vector<int> v = {1, 2, 3, 4};
    cout << S.findUnsortedSubarray(v) << endl;
}
