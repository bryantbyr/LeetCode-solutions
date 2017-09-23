//219. Contains Duplicate II.cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

//Created by bryantbyr on 20170923
//Time:O(n)
//Space:O(n)
//array + unordered_map
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (map.find(nums[i]) != map.end() && i - map[nums[i]] <= k)//"map[nums[i]] - i" VS "i - map[nums[i]]"
                return true;
            map[nums[i]] = i;
        }
        return false;
    }
};

//Created by bryantbyr on 20170923
//Time:O(n)
//Space:O(n)
//array + unordered_set
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> set;
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (i > k)
                set.erase(nums[i - k - 1]);
            if (set.find(nums[i]) != set.end())
                return true;
            set.insert(nums[i]);
        }
        return false;
    }
};

int main()
{
    Solution S;
    vector<int> v = {2, 1, 6, 3, 4, 2, 7, 4};
    cout << S.containsNearbyDuplicate(v, 4) << endl;
}
