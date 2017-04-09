//47-Permutations II_Be Better.cpp

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

//20170325
//Time:O(N^2)
//Space:O(1)
//Backtracking is OK
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
//            if(!isExit(r,nums))
                r.push_back(nums);
        }
        else{
        	int min=*min_element(begin(nums),end(nums));
        	int max=*max_element(begin(nums),end(nums));
        	vector<bool> b(max-min+1,false);
            for(int i=t;i<n;i++){
                if(!b[nums[i]-min]||i==t){
                    b[nums[i]-min]=1;
                    swap(nums[i],nums[t]);
                    backTracking(t+1,nums.size(),r,nums);
                    swap(nums[i],nums[t]);
                }
            }
        }
    }
};

int main()
{
    Solution s;
    vector<int> v={3,3,0,0,2,3,2};
    vector<vector<int>> r=s.permuteUnique(v);
    for(int i=0;i<r.size();i++){
        for(int k=0;k<r[i].size();k++)
            cout<<r[i][k];
        cout<<endl;
    }

    return 0;
}

