//645. Set Mismatch.cpp
#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

//Created by bryantbyr on 20171009
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> res;
        unordered_map<int, int> map;
        for (int num : nums) {
            if (++map[num] == 2)
                res.push_back(num);
        }
        for (int i = 1; i <= nums.size(); i++) {
            if (map.find(i) == map.end())
                res.push_back(i);
        }
        return res;
    }
};

//Created by bryantbyr on 20171009
//Time:O(n*log(n))
//Space:O(1)
//Sort
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int repeat = 0, miss = nums[0] == 2 ? 1 : 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1])
                repeat = nums[i - 1];
            else if (nums[i] - nums[i - 1] == 2)
                miss = nums[i] - 1;
        }
        miss = (miss == 0) ? nums.size() : miss;
        return {repeat, miss};
    }
};

//Created by bryantbyr on 20171009
//Time:O(n)
//Space:O(1)
//Once Loop
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int repeat = 0, miss = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[abs(nums[i]) - 1] < 0)
                repeat = abs(nums[i]);
            else
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1];
        }
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0)
                miss = i + 1;
        }
        return {repeat, miss};
    }
};

//Learn from discuss on 20171009
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int sum = 0;
        unordered_set<int> set;
        int repeat = 0, miss = 0;
        for (int num : nums) {
            if (set.find(num) != set.end())
                repeat = num;
            set.insert(num);
            sum += num;
        }
        int n = nums.size();
        return {repeat, n*(n + 1) / 2 - sum + repeat};
    }
};

//Learn from discuss on 20171009
//Time:O(n)
//Space:O(1)
//Once Loop
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int repeat = 0, miss = 0;
        for (unsigned i = 0; i < nums.size(); ++i) {
            while (nums[i] != nums[nums[i] - 1])
                swap(nums[i], nums[nums[i] - 1]);
        }
        for (unsigned i = 0; i < nums.size(); ++i) {
            if (nums[i] != i + 1) {
                repeat = nums[i];
                miss = i + 1;
            }
        }
        return {repeat, miss};
    }
};

//Learn from discuss on 20171009
//Time:O(n)
//Space:O(1)
//Once Loop + bitwise
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        vector<int> v(n, 0);
        int repeat = 0, miss = 0;
        for (int i = 0; i < n; ++i) {
            miss ^= (i + 1) ^ nums[i];
            if (++v[nums[i] - 1] == 2)
                repeat = nums[i];
        }
        miss ^= repeat;
        return {repeat, miss};
    }
};

int main()
{
    Solution S;
    vector<int> v = {8, 7, 3, 5, 3, 6, 1, 4};
    vector<int> r = S.findErrorNums(v);
    for (unsigned i = 0; i < r.size(); ++i) {
        cout << r[i] << endl;
    }
}
