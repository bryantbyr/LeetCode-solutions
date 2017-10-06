//575. Distribute Candies.cpp
#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <bitset>
using namespace std;

//Created by bryantbyr on 20171006
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        unordered_set<int> set;
        for (int candy : candies)
            set.insert(candy);
        return min(candies.size() / 2, set.size());
    }
};

//Learn from discuss on 20171006
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        unordered_set<int> set(candies.begin(), candies.end());
        return min(candies.size() >> 1, set.size());
    }
};

//Learn from discuss on 20171006
//Time:O(n)
//Space:O(n)
//bitset
class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        bitset<200001> hash;
        for (unsigned i = 0; i < candies.size(); ++i) {
            if (!hash.test(candies[i] + 100000))
                hash.set(candies[i] + 100000);
        }
        return min(hash.count(), candies.size() >> 1);
    }
};

int main()
{
    Solution S;
    vector<int> v = {1, 1, 2, 2, 3, 3};
    cout << S.distributeCandies(v) << endl;
}
