//611. Valid Triangle Number.cpp
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

//Created by bryantbyr on 20171004
//Time:O(n^3)
//Space:O(1)
//array (Note:组合数计算时越界 Runtime Error)
// class Solution {
// public:
//     int C(int c, int n) {
//         int res;
//         int t1 = c;
//         int t2 = n;
//         int t3 = c - n == 0 ? 1 : c - n;
//         int t4 = t3;
//         while (c != 1)
//             t1 *= --c;
//         while (n != 1)
//             t2 *= --n;
//         while (t4 != 1)
//             t3 *= --t4;
//         return t1 / t2 / t3;
//     }
//     int triangleNumber(vector<int>& nums) {
//         int res = 0;
//         sort(nums.begin(), nums.end());
//         for (int i = nums.size() - 1; i > 1 ; --i) {
//             int cnt = 0;
//             for (int j = 0; j < i; ++j) {
//                 int k = j + 1;
//                 for (; k < i; ++k) {
//                     if (nums[j] + nums[k] > nums[i])
//                         break;
//                     cnt++;
//                 }
//                 if (k - j == 1)
//                     break;
//             }
//             res += C(i, 2) - cnt;
//         }
//         return res;
//     }
// };

//Created by bryantbyr on 20171004
//Time:O(n^3)
//Space:O(1)
//array
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int res = 0;
        sort(nums.begin(), nums.end());
        for (int i = nums.size() - 1; i > 1 ; --i) {
            for (int j = 0; j < i - 1; ++j) {
                for (int k = j + 1; k < i; ++k) {
                    if (nums[j] + nums[k] > nums[i])
                        res++;
                }
            }
        }
        return res;
    }
};

//Created by bryantbyr on 20171004
//Time:O(n^3)
//Space:O(1)
//array (Note: Time Limit Exceeded)
// class Solution {
// public:
//     int triangleNumber(vector<int>& nums) {
//         int res = 0;
//         for (int i = nums.size() - 1; i > 1 ; --i) {
//             for (int j = 0; j < i - 1; ++j) {
//                 for (int k = j + 1; k < i; ++k) {
//                     // if (nums[i] == 0 || nums[j] == 0 || nums[k] == 0)
//                     //     continue;
//                     // if (nums[j] + nums[k] + nums[i] - max(max(nums[j], nums[k]), nums[i]) > max(max(nums[j], nums[k]), nums[i]))
//                     //     res++;
//                     if (nums[j] + nums[k] > nums[i] && nums[j] + nums[i] > nums[k] && nums[i] + nums[k] > nums[j])
//                         res++;
//                 }
//             }
//         }
//         return res;
//     }
// };

//Learn from discuss on 20171005
//Time:O(n^2)
//Space:O(1)
//array
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int res = 0;
        sort(nums.begin(), nums.end());
        for (int i = nums.size() - 1; i > 1 ; --i) {
            int l = 0, r = i - 1;
            while (l < r) {
                if (nums[l] + nums[r] > nums[i]) {
                    res += r - l;
                    r--;
                }
                else
                    l++;
            }
        }
        return res;
    }
};


int main()
{
    Solution S;
    vector<int> v = {82, 15, 23, 82, 67, 0, 3, 92, 11};
    // vector<int> v = {16, 70, 16, 36, 17, 39, 44, 72, 25, 88, 18, 22, 20, 84, 18, 66, 71, 74, 87, 59, 48, 91, 52, 15, 92, 29, 85, 21, 10, 34, 86, 68, 10, 27, 3, 42, 49, 48, 18, 15, 6, 39, 61, 28, 19, 52, 60, 8, 37, 32, 71, 82, 54, 38, 47, 33, 10, 64, 52, 71, 39, 63, 64, 79, 86, 47, 16, 72, 55, 17, 35, 88, 74, 93, 10, 59, 3, 64, 95, 91, 61, 28, 63, 23, 49, 6, 24, 47, 41, 88, 96, 23, 90, 53, 84, 3, 35, 23, 3, 17};
    cout << S.triangleNumber(v) << endl;
}
