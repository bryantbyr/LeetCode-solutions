//80. Remove Duplicates from Sorted Array II.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170909
//Time:O(n)
//Sapce:O(1)
//Two Pointers !: 只正确计算出了数组长度,未得到正确的数组
// class Solution {
// public:
//     int removeDuplicates(vector<int>& nums) {
//         int count = 0;
//         for (int i = 0; i < (int)nums.size();) {
//             int j = i + 2;
//             while (j < (int)nums.size() && nums[i] == nums[j]) {
//                 j++;
//                 count++;
//             }
//             i = nums[i] == nums[i + 1] ? j : i + 1;
//         }
//         return nums.size() - count;
//     }
// };

//Learn from discuss on 20170909
//Time:O(n)
//Space:O(1)
//Two Pointers
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size(), count = 0;
        for (int i = 2; i < n ; i++)
            if (nums[i] == nums[i - 2 - count])
                count++;
            else
                nums[i - count] = nums[i];
        return n - count;
    }
};

//Learn from discuss on 20170909
//Time:O(n)
//Space:O(1)
//Two Pointers
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        for (int n : nums)
            if (i < 2 || n > nums[i - 2])
                nums[i++] = n;
        return i;
    }
};

int main()
{
    Solution s;
    vector<int> v = {1, 2, 2, 4};
    cout << s.removeDuplicates(v) << endl;
    cout << "The array is: " << endl;
    for (unsigned i = 0; i < v.size(); ++i) {
        cout << v[i] << endl;
    }
}
