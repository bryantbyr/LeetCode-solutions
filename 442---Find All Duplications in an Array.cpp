//442-Find All Duplications in an Array.cpp

//learn from group

#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
    vector<int> findDumplications(vector<int>& nums){
        //int* res=new int[nums.size()];
        vector<int> res;
        int i=0;
        for(;i<nums.size();i++)
        { 
			int temp=nums[i];
			while(temp>nums.size())
				temp-=nums.size();     
		    nums[temp-1]+=nums.size();
            if(nums[temp-1]>2*nums.size())
                res.push_back(temp);
        }
        return res;
    }
};

int main()
{
    Solution s;
    vector<int> a;
    a.resize(8);
    a={4,3,2,7,8,2,3,1};
    vector<int> r=s.findDumplications(a);
    int k=0;
    for(;k<r.size();k++)
        cout<<r[k]<<endl;
    return 0;
}
