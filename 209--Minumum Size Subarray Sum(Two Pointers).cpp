//209--Minumum Size Subarray Sum(Two Pointers).cpp

#include<iostream>
#include<vector>
using namespace std;

//Learn From Others
//Time complexity:O(N)
//Space complexity:O(1)
//Two Pointers
class Solution{
public:
    int minSubArrayLen(int s,vector<int>& nums)
    {
        if(nums.size()==0)
            return 0;

        int i=0,j=0,sum=0,len=INT_MAX;
        for(;i<nums.size();i++){
            sum+=nums[i];
            while(sum>=s){
                sum-=nums[j++];
                len=i-j+2>len?len:i-j+2;
            }
        }
        return len<=nums.size()?len:0;
    }
};

int main()
{
    Solution s;
    vector<int> v;

    v={12,28,83,4,25,26,25,2,25,25,25,12};
    cout<<s.minSubArrayLen(213,v)<<endl;

    return 0;
}
