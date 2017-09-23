//35. Search Insert Position.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170923
//Time:O(n)
//Space:O(1)
//array (insert)
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (nums[i] >= target)
                return i;
        }
        return nums.size();
    }
};

//Created by bryantbyr on 20170923
//Time:O(n)
//Space:O(1)
//Binary Search
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] > target)
                end = mid - 1;
            else if (nums[mid] < target)
                start = mid + 1;
            else
                return mid;
        }
        return start;
    }
};

//Learn from discuss on 20170923
//Time:O(n)
//Space:O(1)
//Binary Search
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return low;
    }
};

int main()
{
    Solution S;
    vector<int> v = {1, 3, 5, 6};
    cout << S.searchInsert(v, 2) << endl;
}
