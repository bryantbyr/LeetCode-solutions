//70. Climbing Stairs.cpp
#include <iostream>
#include <vector>

//Created by bryantbyr on 20170818
//Time:O(n)
//Space:O(n)
//DP
class Solution {
public:
    int climbStairs(int n) {
        std::vector<int> v(n+1,0);
        v[1]=v[0]=1;
        for(int i=2;i<=n;i++)
            v[i]=v[i-2]+v[i-1];
        return v[n];
    }
};

int main()
{
    Solution s;
    std::cout<<s.climbStairs(3)<<std::endl;
}
