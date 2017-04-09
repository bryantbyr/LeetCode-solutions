//75-Sort Colors.cpp

#include<iostream>
#include<vector>
using namespace std;

//2017/03/20
//Time:O(N)
//Space:O(1)
//Two Pointers
class Solution{
public:
    void sortColors(vector<int>& nums)
    {
        int i=-1,j=0,count=1;
        for(int k=0;k<nums.size();k++){
            if(nums[k]==0){
                i++;
                Insert(nums,k,i);
            }
            else if(nums[k]==1){
                j=i+count;
                Insert(nums,k,j);
                count++;
            }
        }
    }
    void Insert(vector<int>& nums,int target,int pos)
    {
        int temp=nums[target];
        while(target>pos)
            nums[target]=nums[--target];
        nums[pos]=temp;
    }
};

int main()
{
    Solution s;
    std::vector<int> v;
    v={0,1};
    s.sortColors(v);

    for(int i=0;i<v.size();i++){
        cout<<v[i]<<endl;
    }

    return 0;
}
