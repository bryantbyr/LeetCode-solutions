//283-Move Zeroes(Two Pointers).cpp

#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
    void moveZeroes(vector<int>& nums)
    {
        int i=0,j=0,key=0;
        for(;i<nums.size();i++){
            if(nums[i]!=0&&key==1)
                swap(nums[i],nums[j++]);
            else if(nums[i]==0&&key==0){
                j=i;
                key=1;
            }
        }
    }
};

int main()
{
    Solution s;
    vector<int> v;
    v={1,0,1};
    s.moveZeroes(v);
    for(int i=0;i<v.size();i++)
        cout<<v[i]<<endl;

    return 0;
}
