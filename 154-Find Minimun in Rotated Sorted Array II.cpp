//154-Find Minimun in Rotated Sorted Array II.cpp

#include<iostream>
#include<vector>
using namespace std;

//Author:bryantbyr
//Time complexity:O(n)
//暴力遍历
class Solutiuon{
public:
    int findMin(vector<int>& nums)
    {
        if(nums.size()==0)
            return false;
        if(nums[0]<nums[nums.size()-1])
            return nums[0];

        int i=0,j=nums.size()-1;
        for(;i<nums.size()-1&&j>0;i++,j--){
            if(nums[i+1]<nums[i])
                break;
            if(nums[j-1]>nums[j])
                break;
        }
        return i>=(nums.size()-1)?nums[i]:min(nums[i+1],nums[j]);
    }
};

int main()
{
    Solutiuon s;
    vector<int> v;
    v={5,6,6,7,8,2,3,4,4};
    //v={3,1,3};
    cout<<s.findMin(v)<<endl;

    return 0;
}
