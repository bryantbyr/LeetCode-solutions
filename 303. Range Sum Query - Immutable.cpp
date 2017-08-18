//303. Range Sum Query - Immutable.cpp
#include <iostream>
#include <vector>
using namespace std;

//20170818
//Time:O(n)
//Space:O(n)
//DP
class NumArray {
public:
    NumArray(vector<int> nums) {
        // int t=0;
        // sum.push_back(0);
        // for(unsigned int i=1;i<=nums.size();i++){
        //     sum.push_back(t+nums[i-1]);
        //     t=sum[i];
        // }
        sum = nums;
    }

    int sumRange(int i, int j) {
        int r=0;
        for(int k=i;k<=j;k++)
            r+=sum[k];
        return r;
    }
private:
    vector<int> sum;
};

int main()
{
    vector<int> nums = { -2, 0, 3, -5, 2, -1};
    NumArray* obj = new NumArray(nums);
    cout << obj->sumRange(2, 5) << endl;;
}
