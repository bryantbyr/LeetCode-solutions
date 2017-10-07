//599. Minimum Index Sum of Two Lists.cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

//Created by bryantbyr 20171007
//Time:O(n+m)
//Space:(n)
//Hash Table
class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string, int> map1;
        vector<string> r;
        int sum = 0, res = INT_MAX;
        for (unsigned i = 0; i < list1.size(); ++i)
            map1[list1[i]] = i;
        for (unsigned i = 0; i < list2.size(); ++i) {
            if (map1.find(list2[i]) != map1.end()) {
                sum = map1[list2[i]] + i;
                if (sum < res) {
                    res = sum;
                    // while (r.size() != 0)
                    //     r.pop_back();
                    r.clear();
                    r.push_back(list2[i]);
                }
                else if (sum == res)
                    r.push_back(list2[i]);
            }
        }
        return r;
    }
};


int main()
{
    Solution S;
    vector<string> list1 = {"Shogun", "Tapioca Express", "Burger King", "KFC"};
    vector<string> list2 = {"KFC", "Shogun", "Burger King"};
    vector<string> res = S.findRestaurant(list1, list2);
    for (unsigned i = 0; i < res.size(); ++i)
        cout << res[i] << endl;
}
