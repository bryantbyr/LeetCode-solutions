//75-Sort Colors_version.2.cpp

#include<iostream>
#include<vector>
using namespace std;

//2017/03/20
//Time:O(N)
//Space:O(1)
//General way
class Solution{
public:
    void sortColors(vector<int>& nums)
    {
        int i=0,j=0;
        for(int k=0;k<nums.size();k++){
            if(nums[k]==0)
                i++;
            else if(nums[k]==1)
                j++;
        }
        for(int k=0;k<nums.size();k++){
            if(k<i)
                nums[k]=0;
            else if(k<i+j)
                nums[k]=1;
            else
                nums[k]=2;
        }
    }
};

int main()
{
    Solution s;
    std::vector<int> v;
    v={0,2,2,1,0,1};
    s.sortColors(v);

    for(int i=0;i<v.size();i++){
        cout<<v[i]<<endl;
    }

    return 0;
}
