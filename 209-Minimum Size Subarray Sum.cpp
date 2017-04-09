//209-Minimum Size Subarray Sum.cpp

#include<iostream>
#include<vector>
using namespace std;

//Author:bryantbyr
//Time complexity:O(N^2)
//Space complexity:O(1)
//暴力求解
class Solution{
public:
    int minSubArrayLen(int s,vector<int>& nums)
    {
		int temp;
        int count=nums.size()+1;
        for(int i=0;i<nums.size();i++){
    		temp=nums[i];
            int k=i;
            while(temp<s){
            	if(k>=nums.size()-1)
            		break;
            	temp+=nums[++k];
			}
            if(temp>=s&&count>(k-i+1))
                count=k-i+1;
        }
        if(count==nums.size()+1)
            return 0;
        else
            return count;
    }
};

int main()
{
    Solution s;
    vector<int> v;
    v={1,2,3,4,5};
    cout<<s.minSubArrayLen(15,v)<<endl;

    return 0;
}
