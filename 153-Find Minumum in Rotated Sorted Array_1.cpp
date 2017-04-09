//153-Find Minumum in Rotated Sorted Array_1.cpp

#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
    int findMin(vector<int>& nums)
    {
        if(nums.size()==0)
            return 0;

        if(nums[0]<=nums[nums.size()-1])
            return nums[0];

        int k=0;
        for(;k<nums.size()-1;k++){
            if(nums[k+1]<nums[k])
                break;
        }
        return nums[k+1];
    }

};

int main()
{
    Solution s;
    vector<int> v;
    v={4,5,6,7};
    //v={1};
    cout<<s.findMin(v)<<endl;

    return 0;
}
