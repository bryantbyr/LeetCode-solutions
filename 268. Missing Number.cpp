//268. Missing Number.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170906
//Time:O(n)
//Space:O(n)
//vector (map)
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        vector<int> m(n + 1, 0);
        for (int i = 0; i < n; ++i)
            m[nums[i]] = 1;
        for (int i = 0; i < n + 1; ++i)
            if (m[i] == 0)
                return i;
        return -1;
    }
};

int main()
{
    Solution S;
    vector<int> v = {1};
    cout << S.missingNumber(v) << endl;
}
