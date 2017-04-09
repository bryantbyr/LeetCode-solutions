//172-Factorial Trailing Zeroes.cpp

//learn from group

#include<iostream>
using namespace std;

class Solution{
    public:
        int trailingZeroes(int n){
            int count=0;
            while(n>=5){
                count+=n/5;
                n=n/5;
            }
            return count;
        }
};

int main()
{
    Solution s;
    cout<<s.trailingZeroes(1808548329)<<endl;
    return 0;
}
