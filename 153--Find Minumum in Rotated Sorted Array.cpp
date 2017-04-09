//153-Find Minumum in Rotated Sorted Array.cpp

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

        int start=0,end=nums.size()-1;
        while(start<=end){
            int middle=start+(end-start)/2;
            if(nums[middle]>nums[start])
                start=middle;
            else if(nums[middle]<nums[start])
                end=middle;
            else
                break;
        }
        //return nums[start]>nums[end]?nums[end]:nums[start];
        return min(nums[start],nums[end]);
    }

};

int main()
{
    Solution s;
    vector<int> v;
    v={2,3,1};
    //v={1};
    cout<<s.findMin(v)<<endl;

    return 0;
}
