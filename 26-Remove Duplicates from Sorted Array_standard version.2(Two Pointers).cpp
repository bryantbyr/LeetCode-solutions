//26-Remove Duplicates from Sorted Array_standard version.2(Two Pointers).cpp

#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
    int removeDuplicates(vector<int>& nums){
        if(nums.size()==0)
            return 0;
        int j=0,count=0;
        vector<int> pos(INT_MAX/10000,-1);
        for(int i=0;i<nums.size();i++){
            if(pos[nums[i]+INT_MAX/30000]==-1){
            	pos[nums[i]+INT_MAX/30000]=i;
                nums[j++]=nums[i];
            }

        }
        return j;
    }
};

int main()
{
    Solution s;
    std::vector<int> v;
    v={1,1,2,4,2,3};
    cout<<s.removeDuplicates(v)<<endl;

    return 0;
}
