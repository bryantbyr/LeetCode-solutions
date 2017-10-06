//136. Single Number.cpp
#include <iostream>
#include <vector>
using namespace std;

//Lean from discuss on 20171006
//Time:O(n)
//Space:O(1)
//bitwise
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (unsigned i = 0; i < nums.size(); ++i)
            res ^= nums[i];
        return res;
    }
};

int main()
{
    Solution S;
    vector<int> v = {1, 1, 2, 4, 2};
    cout << S.singleNumber(v) << endl;
}
