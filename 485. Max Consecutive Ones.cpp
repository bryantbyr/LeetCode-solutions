//485. Max Consecutive Ones.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170919
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int r = 0, count = 0;
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                count++;
                r = max(count, r);
            }
            else
                count = 0;
        }
        return r;
    }
};

int main()
{
    Solution S;
    vector<int> v = {1, 1, 0, 1, 1, 1};
    cout << S.findMaxConsecutiveOnes(v) << endl;
}
