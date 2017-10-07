//202. Happy Number.cpp
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

//Created by bryantbyr on 20171007
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
public:
    int dealNumber(int n) {
        int res = 0;
        while (n != 0) {
            res += (n % 10) * (n % 10);
            n /= 10;
        }
        return res;
    }
    bool isHappy(int n) {
        unordered_set<int> set;
        while (n != 1) {
            n = dealNumber(n);
            if (set.find(n) != set.end())
                return false;
            set.insert(n);
        }
        return true;
    }
};

//Learn from discuss on 20171007
//Time:O(n)
//Space:O(1)
//Math
class Solution {
public:
    bool isHappy(int n) {
        while (n > 6) {
            int next = 0;
            while (n) {
                next += (n % 10) * (n % 10);
                n /= 10;
            }
            n = next;
        }
        return n == 1;
    }
};

//Learn from discuss on 20171007
//Time:O(n)
//Space:O(1)
//Two Pointers
class Solution {
public:
    int dealNumber(int n) {
        int res = 0;
        while (n != 0) {
            res += (n % 10) * (n % 10);
            n /= 10;
        }
        return res;
    }
    bool isHappy(int n) {
        int slow = n, fast = n;
        do {
            slow = dealNumber(slow);
            fast = dealNumber(fast);
            fast = dealNumber(fast);
        } while (slow != fast);
        return slow == 1;
    }
};

int main()
{
    Solution S;
    cout << S.isHappy(19) << endl;
}
