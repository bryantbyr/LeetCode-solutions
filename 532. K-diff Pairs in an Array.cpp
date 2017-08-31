//532. K - diff Pairs in an Array.cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
using namespace std;

//Created by bryantbyr on 20170831
//Time:O(n^2)
//Space:O(1)
//Two Pointers
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        int count = 0;
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            if (nums[r] - nums[l] > k)
                r--;
            else if (nums[r] - nums[l] < k) {
                int temp = nums[l];
                l++;
                while (nums[l] == temp) l++;
                r = nums.size() - 1;
            }
            else if (l != r) {
                count++;
                int temp = nums[l];
                l++;
                while (nums[l] == temp) l++;
                r = nums.size() - 1;
            }
            else {
                int temp = nums[l];
                l++;
                while (nums[l] == temp) l++;
                r = nums.size() - 1;
            }
        }
        return count;
    }
};

//Created by bryantbyr on 20170831
//Time:O(n^2)
//Space:O(1)
//Two Pointers
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        int count = 0;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < (int)nums.size();) {
            for (int j = i + 1; j < (int)nums.size(); j++) {
                if (nums[j] - nums[i] == k) {
                    count++;
                    break;
                }
                else if (nums[j] - nums[i] > k) {
                    break;
                }
            }
            int temp = nums[i];
            i++;
            while (nums[i] == temp) i++;
        }
        return count;
    }
};

//Learn from discuss on 20170831
//Time:O(n)
//Space:O(n)
//unordered_set + unordered_map
class Solution {
public:
    /**
     * for every number in the array:
     *  - if there was a number previously k-diff with it, save the smaller to a set;
     *  - and save the value-index to a map;
     */
    int findPairs(vector<int>& nums, int k) {
        if (k < 0) {
            return 0;
        }
        unordered_set<int> starters;
        unordered_map<int, int> indices;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (indices.count(nums[i] - k)) {
                starters.insert(nums[i]);
            }
            if (indices.count(nums[i] + k)) {
                starters.insert(nums[i] + k);
            }
            indices[nums[i]] += 1;
        }
        return starters.size();
    }
};

//Learn from discuss on 20170831
//Time:O(n)
//Space:O(n)
//unordered_map
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        int result = 0;
        if (k < 0) return result;
        for (int num : nums) {
            map[num]++;
        }
        for (std::pair<int, int> p : map) {
            if (k == 0) {
                if ( p.second > 1) result++;
            } else {
                if (map.find(p.first + k) != map.end()) result++;
            }
        }
        return result;
    }
};

int main()
{
    Solution s;
    vector<int> v = {3, 1, 4, 1, 5}; // 1,1,3,4,5
    cout << s.findPairs(v, 2) << endl;
}
