#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//Created by bryantbyr on 20170815
//array基本操作
//Time:O(n)
//Space:O(1)
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        if(!digits.size())
            return {};
        int m=digits.size();
        vector<int> t;
        int add=1;
        for (int i = m-1; i >=0; --i)
        {
            int k=(digits[i]+add)%10;
            if(k==0&&add==1)
                add=1;
            else
                add=0;
            t.push_back(k);
        }
        if(add==1)
            t.push_back(1);
        reverse(t.begin(),t.end());
        return t;
    }
};


int main()
{
    Solution s;
    vector<int> t={9};
    vector<int> r=s.plusOne(t);
    for (unsigned int i = 0; i < r.size(); ++i)
        cout<<r[i]<<"  ";
}
