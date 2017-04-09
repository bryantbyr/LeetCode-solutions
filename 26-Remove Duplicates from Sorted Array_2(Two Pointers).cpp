//26-Remove Duplications from Sorted Array_2(Two Pointers).cpp

#include<iostream>
#include<vector>
using namespace std;

//2017/03/20
//Time:O(n)
//Space:O(1)
//Two Pointers
class Solution{
public:
    int removeDuplicates(vector<int>& nums)
    {
        int n=nums.size();
        int count=0;
        for(int i=1;i<nums.size();i++){
            if(nums[i]!=nums[i-1])
                nums[i-count]=nums[i];
            else
                count++;
        }

        return n-count;
    }
};

int main()
{
    Solution s;
    vector<int> v;
    v={1,2};
    cout<<s.removeDuplicates(v)<<endl;

    return 0;
}
