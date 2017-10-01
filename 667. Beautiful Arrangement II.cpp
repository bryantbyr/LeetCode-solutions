//667. Beautiful Arrangement II.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20171001
//Time:O(n^2)
//Space:O(1)
//array
class Solution {
public:
    bool isExit(vector<int>& v, int index, int target) {
        for (int i = 0; i < index; ++i) {
            if (v[i] == target)
                return true;
        }
        return false;
    }
    vector<int> constructArray(int n, int k) {
        vector<int> res(n, 0);
        for (int i = 0; i < n; i++)
            res[i] = i + 1;
        int dif = k;
        res[0] = 1;
        for (int i = 1; i < k + 1; ++i) {
            if (res[i - 1] - dif > 1 && !isExit(res, i, res[i - 1] - dif))
                res[i] = res[i - 1] - dif;
            else
                res[i] = res[i - 1] + dif;
            dif--;
        }
        return res;
    }
};

//Learn from discuss on 20171001
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> res(n, 1);
        for (int i = 1; i < n; i++)
            res[i] = i + 1;
        int dif = k;
        bool key = true;
        for (int i = 1; i < k + 1; ++i) {
            if (key) {
                res[i] = res[i - 1] + dif;
                key = false;
            }
            else {
                res[i] = res[i - 1] - dif;
                key = true;
            }
            dif--;
        }
        return res;
    }
};

//Learn from discuss on 20171001
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> res;
        int l = 1, r = k + 1;
        while (l < r) {
            res.push_back(l++);
            res.push_back(r--);
            if (l == r)
                res.push_back(l);
        }
        for (int i = k + 2; i <= n; i++)
            res.push_back(i);
        return res;
    }
};

//Learn from discuss on 20171001
//Time:O(n)
//Space:O(1)
//array
class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> res;
        for (int i = 1, j = n; i <= j; )
            res.push_back(k > 1 ? (k-- % 2 ? i++ : j--) : i++);
        return res;
    }
};

int main()
{
    Solution S;
    vector<int> r = S.constructArray(5, 4);
    for (unsigned i = 0; i < r.size(); ++i)
        cout << r[i] << endl;
}
