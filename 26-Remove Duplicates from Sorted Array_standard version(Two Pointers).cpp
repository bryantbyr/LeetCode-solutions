//26-Remove Duplicates from Sorted Array_standard version(Two Pointers).cpp

#include<iostream>
#include<vector>
using namespace std;

//2017/03/20
//Time:O(N)
//Space:O(1)
//Two Pointers
class Solution{
public:
    int removeDuplicates(vector<int>& nums){
    	if(nums.size()==0)
    		return 0;
        int j=1;
        for(int i=1;i<nums.size();i++){
            if(nums[i]!=nums[i-1])
                nums[j++]=nums[i];
        }

        return j;
    }
};

int main()
{
    Solution s;
    std::vector<int> v;
    v={2};
    cout<<s.removeDuplicates(v)<<endl;

    return 0;
}
