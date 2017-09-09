//11. Container With Most Water.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170909
//Time:O(n^2)
//Space:O(1)
//Two Pointers + loop
class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxA = 0;
        int l = 0;
        int r = height.size() - 1;
        for (int i = 0; i < r + 1; i++) {
            while (height[r] < height[i])
                r--;
            while (height[l] < height[i])
                l++;
            maxA = max(maxA, max(i - l, r - i) * height[i]);
            r = height.size() - 1;
            l = 0;
        }
        return maxA;
    }
};

//Learn from discuss on 20170909
//Time:O(n)
//Space:O(1)
//Two Pointers *
class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;
        int maxValue = 0;
        while ( i < j ) {
            int h = min(height[i], height[j]);
            maxValue = max(maxValue, h * (j - i));
            while (height[i] <= h && i < j)
                i++;
            while (height[j] <= h && i < j)
                j--;
        }
        return maxValue;
    }
};

int main()
{
    Solution s;
    vector<int> v = {2, 1, 8, 2, 7, 3};
    cout << s.maxArea(v) << endl;
}
