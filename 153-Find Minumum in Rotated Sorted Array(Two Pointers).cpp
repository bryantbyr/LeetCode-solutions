//153-Find Minumum in Rotated Sorted Array(Two Pointers).cpp

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

        int i=0;
        int j=nums.size()-1;
        for(;i<nums.size()-1&&j>0;i++,j--){
            if(nums[i+1]<nums[i])
                break;
            if(nums[j-1]>nums[j])
                break;
        }
        return min(nums[i+1],nums[j]);
    }

};

int main()
{
    Solution s;
    vector<int> v;
    v={4,5,6,7,1,2,3};
    //v={1};
    cout<<s.findMin(v)<<endl;

    return 0;
}
