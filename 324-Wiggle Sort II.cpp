//324-Wiggle Sort II.cpp

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//20170406
//Time:O(NlogN)
//Space:O(N)
//排序后合并,判断有无不符合条件的点,若存在,以该点位置为支点翻转即可
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<int> r={};
        int k=0,j;
        if(nums.size()%2==0)
            j=nums.size()/2;
        else
            j=nums.size()/2+1;
        for(int i=0;i<nums.size();i++){//将后面的一半元素依次插入到前面一半中
            if(i%2==0){
                r.push_back(nums[k]);
                k++;
            }
            else{
                r.push_back(nums[j]);
                j++;
            }
        }
        int pos=0;
        for(;pos<r.size()-1;pos++){//确定要翻转的支点位置：pos
            if(r[pos]==r[pos+1])
                break;
        }
        int m=0,count=pos;
        for(int k=0;k<nums.size();k++){
            if(k<nums.size()-count-1)
                nums[k]=r[++pos];
            else
                nums[k]=r[m++];
        }
	}
};

int main()
{
    Solution s;
    vector<int> v={1,1,6,6,7,8,6};
    s.wiggleSort(v);
    for(int i=0;i<v.size();i++)
        cout<<v[i]<<endl;
    return 0;
}
