//448. Find All Numbers Disappeared in an Array.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170919
//Time:O(n)
//Space:O(1)
//array (once loop)*
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> r = {};
        for (unsigned i = 0; i < nums.size(); ++i)
            //nums[abs(nums[i]) - 1] = nums[abs(nums[i]) - 1] > 0 ? -nums[abs(nums[i]) - 1] : nums[abs(nums[i]) - 1];
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1]);
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0)
                r.push_back(i + 1);
        }
        return r;
    }
};

int main()
{
    Solution S;
    vector<int> v = {4, 3, 2, 7, 8, 2, 3, 1};
    vector<int> r = S.findDisappearedNumbers(v);
    for (unsigned i = 0; i < r.size(); ++i)
        cout << r[i] << endl;
}
