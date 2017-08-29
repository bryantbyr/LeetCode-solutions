//27. Remove Element.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170829
//Time:O(n^2)
//Space:O(1)
//Two Pointers (the order of elements is cared)
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        unsigned int i = nums.size(), j = 0;
        for (i = 0; j < nums.size() && i < nums.size(); ++i)
            if (nums[i] == val) {
                j = i;
                while (j < nums.size() && nums[j] == val)
                    j++;
                if (j >= nums.size())
                    break;
                swap(nums[i], nums[j]);
            }
        return i;
    }
};

//Created by bryantbyr on 20170829
//Time:O(n)
//Space:O(1)
//Two Pointers (the order of elements is not cared)
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        unsigned int i = 0, j = 0;
        for (; j < nums.size(); ++j)
            if (nums[j] != val){
                nums[i]=nums[j];
                i++;
            }
        return i;
    }
};

int main()
{
    Solution s;
    vector<int> v = {2, 2, 3, 4, 5, 5};
    cout << s.removeElement(v, 5) << endl;
}
