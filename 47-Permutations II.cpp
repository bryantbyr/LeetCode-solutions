//47-Permutations II.cpp

#include<iostream>
#include<vector>
using namespace std;

//20170325
//Time:O(N^a)
//Space:O(1)
//backtracking
class Solution{
public:
    vector<vector<int>> permuteUnique(vector<int>& nums)
    {
        vector<vector<int>> r={};
        backTracking(0,nums.size(),r,nums);
        return r;
    }
    void backTracking(int t,int n,vector<vector<int>>& r,vector<int>& nums)
    {
        if(t==n){
            // vector<int> t;
            // for(int i=0;i<n;i++){
            //     t.push_back(nums[i]);
            // }
            // if(!isExit(r,t))
            //     r.push_back(t);
            if(!isExit(r,nums))
            	r.push_back(nums);
        }
        else{
            for(int i=t;i<n;i++){
                swap(nums[i],nums[t]);
                backTracking(t+1,nums.size(),r,nums);
                swap(nums[i],nums[t]);
            }
        }

    }
    bool isExit(vector<vector<int>>& r,vector<int>& t)
    {
        for(int k=0;k<r.size();k++){
            if(r[k]==t)
                return true;
        }
        return false;

    }
};

int main()
{
    Solution s;
    vector<int> v={};
    vector<vector<int>> r=s.permuteUnique(v);
    for(int i=0;i<r.size();i++){
        for(int k=0;k<r[i].size();k++)
            cout<<r[i][k];
        cout<<endl;
    }

    return 0;
}
