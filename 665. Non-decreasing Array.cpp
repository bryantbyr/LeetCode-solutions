//665. Non-decreasing Array.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170925
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        nums.insert(nums.begin(), INT_MIN);
        nums.push_back(INT_MAX);
        int count = 0;
        for (unsigned i = 1; i < nums.size() - 1; ++i) {
            if (nums[i - 1] > nums[i]) {
                if (nums[i + 1] > nums[i - 1])
                    count ++;
                else
                    return false;
            }
            else if (nums[i] > nums[i + 1] && nums[i + 1] > nums[i - 1]) {
                count++;
                i++;
            }
        }
        return count <= 1;
    }
};

//Learn from discuss on 20170925
//Time:O(n)
//Space:O(1)
//Greedy
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int cnt = 0;
        for (unsigned i = 1; i < nums.size(); ++i) {
            if (nums[i] < nums[i - 1]) {
                cnt++;
                if (i < 2 || nums[i - 2] < nums[i])
                    nums[i - 1] = nums[i];
                else
                    nums[i] = nums[i - 1];
            }
        }
        return cnt <= 1;
    }
};


int main()
{
    Solution S;
    vector<int> v = { 1, 2, 3, 4, 0, 9, 6, 7, 8};
    cout << S.checkPossibility(v) << endl;
}
