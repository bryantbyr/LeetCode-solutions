//561. Array Partition I.cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//Created by bryantbyr on 20170918
//Time:O(nlog(n))
//Space:O(1)
//array (sort)
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int r = 0;
        for (int i = 0; i < (int)nums.size(); i += 2)
            r += nums[i];
        return r;
    }
};

int main()
{
    Solution S;
    vector<int> v = {1, 4, 3, 2};
    cout << S.arrayPairSum(v) << endl;
}
