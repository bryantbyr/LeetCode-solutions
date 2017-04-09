//162-Find Peak Element(Binary Search).cpp

#include<iostream>
#include<vector>
using namespace std;

//2017/03/18
//Time:O(logN)
//Space:O(1)
//General Binary Search
class Solution{
public:
    int findPeakElement(vector<int>& nums)
    {
        if(nums.size()==0)
            return false;

        int start=0,end=nums.size()-1;
        while(start<end-1){
            int middle=start+(end-start)/2;
            if(nums[middle]>nums[middle-1]&&nums[middle]>nums[middle+1])
                return middle;
            else if(nums[middle]>nums[middle+1])
                end=middle-1;
            else
                start=middle+1;
        }

		if(start==end)
			return start;
		else if(nums[start]>nums[end])
			return start;
		else
			return end;
    }
};

int main()
{
    Solution s;
    vector<int> v;
    v={1,2,3,1};
    cout<<s.findPeakElement(v)<<endl;

    return 0;
}
