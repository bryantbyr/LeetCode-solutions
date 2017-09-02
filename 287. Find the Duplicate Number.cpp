//287. Find the Duplicate Number.cpp
#include <iostream>
#include <vector>
using namespace std;

//Learn from discuss on 20170902
//Time:O(n)
//Space:O(1)
//Two Pointers (cycle)
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if (nums.size() <= 1)
            return -1;
        int slow = 0, fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        slow = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};

//Learn from discuss on 20170902
//Time:O(nlog(n))
//Space:O(1)
//Binary Search
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int start=1;
        int end=nums.size()-1;
        while(start<end){
            int mid=start+(end-start)/2;
            int count=0;
            for(unsigned i = 0; i < nums.size(); ++i) {
                if(nums[i]<=mid)
                count++;
            }
            if(count>mid)
                end=mid;
            else
                start=mid+1;
        }
        return start;
    }
};

int main()
{
    Solution s;
    vector<int> v = {2, 5, 1, 1, 4, 3};
    cout << s.findDuplicate(v) << endl;
}
