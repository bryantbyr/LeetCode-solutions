//26-Remove Duplications from Sorted Array(Two Pointers).cpp

#include<iostream>
#include<vector>
using namespace std;

//2017/03/20
//Time:O(N)
//Space:O(INT_MAX/1000)
//Two Pointers(is applicable for any general array)
class Solution{
public:
    int removeDuplicates(vector<int>& nums)
    {
    	if(nums.size()==0)
    		return 0;
    	if(nums.size()==1)
    		return 1;
        int i=0,j=0,key=0,count=0;
        vector<int> pos(INT_MAX/1000,-1);
        for(;i<nums.size();i++){
        	if(pos[nums[i]+INT_MAX/3000]==-1){
                pos[nums[i]+INT_MAX/3000]=i;
                swap(nums[i],nums[j++]);
            }
            else if(pos[nums[i]+INT_MAX/3000]>-1&&key==0){
                j=i;
                key=1;
                count++;
            }
			else
				count++;
        }

        return nums.size()-count;
    }


};

int main()
{
    Solution s;
    vector<int> v;
    v={-3,-1,0,0,0,3,3};
    cout<<s.removeDuplicates(v)<<endl;

    return 0;
}

