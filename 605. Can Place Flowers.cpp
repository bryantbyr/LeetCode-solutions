//605. Can Place Flowers.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170924
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (flowerbed.size() == 1) {
            if (n == 0 || flowerbed[0] == 0)
                return true;
            else
                return false;
        }
        for (unsigned i = 0; i < flowerbed.size(); ++i) {
            if (i == 0 ) {
                if (flowerbed[i] == 0 && flowerbed[i + 1] == 0) {
                    flowerbed[i] = 1;
                    n--;
                }
            }
            else if (i == flowerbed.size() - 1) {
                if (flowerbed[i - 1] == 0 && flowerbed[i] == 0) {
                    flowerbed[i] = 1;
                    n--;
                }
            }
            else if (flowerbed[i] == 0 && flowerbed[i - 1] == 0 && flowerbed[i + 1] == 0) {
                flowerbed[i] = 1;
                n--;
            }
            if (n <= 0)
                return true;
        }
        return false;
    }
};

//Learn from discuss on 20170924
//Time:O(n)
//Space:O(1)
//array*
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);
        for (int i = 1; i < flowerbed.size() - 1; ++i) {
            if (flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1] == 0) {
                --n;
                ++i;
            }
            if (n <= 0)
                return true;
        }
        return false;
    }
};

//Learn from discuss on 20170924
//Time:O(n)
//Space:O(1)
//array (clean code)
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        for (unsigned i = 0; i < flowerbed.size(); ++i) {
            if ((i == 0 || !flowerbed[i - 1]) && !flowerbed[i] && (i == flowerbed.size() - 1 || !flowerbed[i + 1])) {
                n--;
                //flowerbed[i]=1;
                i++;
            }
            if (n <= 0)
                return true;
        }
        return false;
    }
};

int main()
{
    Solution S;
    vector<int> v = {1, 0, 0, 0, 1};
    cout << S.canPlaceFlowers(v, 1) << endl;
}
