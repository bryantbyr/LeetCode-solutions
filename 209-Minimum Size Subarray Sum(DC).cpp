//209-Minimum Size Subarray Sum(DC).cpp

#include<iostream>
#include<vector>
using namespace std;

//Author:bryantbyr on 2017/3/17
//Time complexity:O(NlogN)
//Space complexity:O(1)
//分治算法（部分思路借鉴于网络+自己创新）
class Solution{
public:
    int minSubArrayLen(int s,vector<int>& nums)
    {
        if(nums.size()==0)return 0;
        return dchelper(nums,s,0,nums.size()-1);
    }
    int dchelper(vector<int>& nums,int s,int left,int right)
    {
        if(left==right)
            return nums[left]>=s?1:0;

        int middle=left+(right-left)/2;
        int leftMin=dchelper(nums,s,left,middle);
        int rightMin=dchelper(nums,s,middle+1,right);

		int minLen=INT_MAX;
		int i=middle;
		int sum=0;
		while(sum<s&&i<=right){
			sum+=nums[i];
			i++;
		}
		int k=middle-1;
		while(sum<s&&k>=left){
			sum+=nums[k];
			k--;
		}
		if(sum<s)
			return 0;

		while(sum>=s)
			sum-=nums[--i];
		sum+=nums[i];
		i++;

		minLen=i-k-1;
		int begin=k-minLen;
		if(begin<left)
			begin=left;
		int finish=i-1;
		int tempLen;
		for(int j=k;j>=begin;j--){
			sum+=nums[j];
			while(sum>=s){
				sum-=nums[finish--];
				tempLen=finish-j+2;
			}
			if(tempLen<=minLen)
				minLen=tempLen;
		}

        return thisMin(leftMin,rightMin,minLen);
    }
    int thisMin(int a,int b,int c)
    {
        if(a==0) a=INT_MAX;
        if(b==0) b=INT_MAX;
        if(a<=b&&a<=c)
            return a;
        else if(b<=a&&b<=c)
            return b;
        return c;
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
