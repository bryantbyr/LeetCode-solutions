//349. Intersection of Two Arrays.cpp
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unsigned int m=0,n=0;
        vector<int> r;
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        while(m<nums1.size()&&n<nums2.size()){
            if(nums1[m]<nums2[n])
                while(nums1[m]<nums2[n])
                    m++;
            else
                while(nums1[m]>nums2[n])
                    n++;
            if(nums1[m]==nums2[n])
                if(r.size()==0||r.back()!=nums1[m])
                    r.push_back(nums1[m]);
            m++;
            n++;
        }
        return r;
    }
};

int main()
{
    Solution S;
    vector<int> v1={3,1,2};
    vector<int> v2={1,1};
    vector<int> r=S.intersection(v1,v2);
    for(unsigned i = 0; i < r.size(); ++i) {
        cout<<r[i]<<endl;
    }

}
