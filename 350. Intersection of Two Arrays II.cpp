//350. Intersection of Two Arrays II.cpp
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170826
//Time:O(nlog(n))
//Space:O(1)
//Two Pointers
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unsigned int m = 0, n = 0;
        vector<int> r;
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        /*
        while (m < nums1.size() && n < nums2.size()) {
            while (nums1[m] < nums2[n]) {
                m++;
                if (m >= nums1.size())
                    return r;
            }
            while (nums1[m] > nums2[n]) {
                n++;
                if (n >= nums2.size())
                    return r;
            }
            if (nums1[m] == nums2[n]) {
                r.push_back(nums1[m]);
                m++;
                n++;
            }
        }
        return r;
        */
        /*
        if (nums1.size() == 0 || nums2.size() == 0)
            return {};
        while (1) {
            while (nums1[m] < nums2[n]) {
                m++;
                if (m >= nums1.size())
                    return r;
            }
            while (nums1[m] > nums2[n]) {
                n++;
                if (n >= nums2.size())
                    return r;
            }
            if (nums1[m] == nums2[n]) {
                r.push_back(nums1[m]);
                if (++m >= nums1.size() || ++n >= nums2.size())
                    return r;
            }
        }
        */
        while (m < nums1.size() && n < nums2.size()) {//(进一步合并化简代码)
            if (nums1[m] < nums2[n])
                m++;
            else if (nums1[m] > nums2[n])
                n++;
            else {
                r.push_back(nums1[m]);
                m++;
                n++;
            }
        }
        return r;
    }
};

int main()
{
    Solution S;
    vector<int> v1 = {1, 2, 2, 1};
    vector<int> v2 = {2, 2};
    vector<int> r = S.intersect(v1, v2);
    for (unsigned int i = 0; i < r.size(); ++i) {
        cout << r[i] << endl;
    }
}
