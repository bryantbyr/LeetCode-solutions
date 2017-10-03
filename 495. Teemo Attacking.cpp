//495. Teemo Attacking.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20171003
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int res = 0;
        int l = 0;
        for (unsigned i = 0; i < timeSeries.size(); ++i) {
            if (i != 0 && timeSeries[i] <= l)
                res += timeSeries[i] + duration - 1 - l;
            else
                res += duration;
            l = timeSeries[i] + duration - 1;
        }
        return res;
    }
};

//Created by bryantbyr on 20171003
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int res = 0;
        for (unsigned i = 0; i < timeSeries.size(); ++i) {
            res += i == 0 ? duration : min(timeSeries[i] - timeSeries[i - 1], duration);
            // if (i != 0 && timeSeries[i] - timeSeries[i - 1] < duration)
            //     res += timeSeries[i] - timeSeries[i - 1];
            // else
            //     res += duration;
        }
        return res;
    }
};

int main()
{
    Solution S;
    vector<int> v = {0, 1, 2, 3, 4};
    cout << S.findPoisonedDuration(v, 1) << endl;
}
