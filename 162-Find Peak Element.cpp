//162-Find Peak Element.cpp

#include<iostream>
#include<vector>
using namespace std;

//2017/03/18
//Time:O(N)
//Brute Force
class Solution{
public:
    int findPeakElement(vector<int>& nums)
    {
        if(nums.size()==0)
            return false;

        int i=0;
        for(;i<nums.size();i++){
            if(i>0&&i<nums.size()-1){
                if(nums[i-1]<nums[i]&&nums[i]>nums[i+1])
                    return i;
            }
            else if(i==nums.size()-1){
                if(nums.size()==1||nums[i-1]<nums[i])
                    return i;
            }
            else if(i==0){
                if(nums.size()==1||nums[i]>nums[i+1])
                    return i;
            }
        }

        return false;
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
