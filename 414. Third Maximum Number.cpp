//414. Third Maximum Number.cpp
#include <iostream>
#include <vector>
#include <set>
using namespace std;

//Learn from discuss on 20170924
//Time:O(n)
//Space:O(1)
//array + set
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> s;
        for (unsigned i = 0; i < nums.size(); ++i) {
            s.insert(nums[i]);
            if (s.size() > 3)
                s.erase(s.begin());
        }
        return s.size() == 3 ? *s.begin() : *s.rbegin();
    }
};

//Created by bryantbyr on 20170929
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int max1 = INT_MIN, k1 = 0;
        int max2 = INT_MIN, k2 = 0;
        int max3 = INT_MIN, k3 = 0;
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (k1 == 0 || nums[i] > max1) {
                max3 = max2;
                max2 = max1;
                max1 = nums[i];
                if (k1 == 1 && k2 == 1)
                    k3 = 1;
                else if (k1 == 1)
                    k2 = 1;
                k1 = 1;
            }
            else if (nums[i] != max1 && (k2 == 0 || nums[i] > max2)) {
                max3 = max2;
                max2 = nums[i];
                if (k2 == 1)
                    k3 = 1;
                k2 = 1;
            }
            else if (nums[i] != max2 && nums[i] != max1 && (k3 == 0 || nums[i] > max3)) {
                max3 = nums[i];
                k3 = 1;
            }
        }
        return k3 ? max3 : max1;
    }
};

//Created by bryantbyr on 20170929
//Time:O(n)
//Space:O(1)
//array*
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int max1 = INT_MIN, k1 = 0;
        int max2 = INT_MIN, k2 = 0;
        int max3 = INT_MIN, k3 = 0;
        for (unsigned i = 0; i < nums.size(); ++i) {
            if ((k1 == 1 && nums[i] == max1) || (k2 == 1 && nums[i] == max2) || (k3 == 1 && nums[i] == max3))
                continue;
            if (k1 == 0 || nums[i] > max1) {
                max3 = max2;
                max2 = max1;
                max1 = nums[i];
                if (k1 == 1 && k2 == 1)
                    k3 = 1;
                else if (k1 == 1)
                    k2 = 1;
                k1 = 1;
            }
            else if (k2 == 0 || nums[i] > max2) {
                max3 = max2;
                max2 = nums[i];
                if (k2 == 1)
                    k3 = 1;
                k2 = 1;
            }
            else if (k3 == 0 || nums[i] > max3) {
                max3 = nums[i];
                k3 = 1;
            }
        }
        return k3 ? max3 : max1;
    }
};

int main()
{
    vector<int> v = {2, 2, 2, 1, 0};
    Solution S;
    cout << S.thirdMax(v) << endl;
}
