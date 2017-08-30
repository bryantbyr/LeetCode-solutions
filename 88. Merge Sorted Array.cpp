//88. Merge Sorted Array.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170830
//Time:O(m+n)
//Space:O(1)
//Merge + Two Pointers (the space of nums1 is not cared)
// class Solution {
// public:
//     void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
//         if (m == 0) {
//             nums1 = nums2;// nums1.assign(nums2.begin(),nums2.end());
//             return;
//         }
//         int j = 0;
//         for ( int i = 0; i < n; i++) {
//             while (nums2[i] > nums1[j]) {
//                 j++;
//                 if (j >= m) {
//                     nums1.insert(nums1.end(), nums2.begin() + i, nums2.end());
//                     return;
//                 }
//             }
//             nums1.insert(nums1.begin() + j, nums2[i]);
//             m++;
//             j++;
//         }
//         return;
//     }
// };

//Learn from discuss on 20170830
//Time:O(m+n)
//Space:O(1)
//Merge + Two Pointers (the space of nums1 is cared)
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1, j = n - 1, k = m + n - 1;
        while (j >= 0) {
            nums1[k--] = i >= 0 && nums1[i] > nums2[j] ? nums1[i--] : nums2[j--];
        }
    }
};

int main()
{
    vector<int> nums1 = {1,0};
    vector<int> nums2 = {2};
    Solution s;
    s.merge(nums1, 1, nums2, 1);
    for (unsigned int i = 0; i < nums1.size(); i++)
        cout << nums1[i] << endl;
}
