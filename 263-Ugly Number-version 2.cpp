//Ugly Number-version 2.cpp
//Run time is 3ms in LeetCode

#include <iostream>
using namespace std;

class Solution{
    public:
        bool isUgly(int num){
            if(num==0)
                return 0;
            while(num%2==0){
                num/=2;
            }
            while(num%3==0){
                num/=3;
            }
            while(num%5==0){
                num/=5;
            }
            return num==1;
        }
};

int main()
{
    Solution s;
    cout<<s.isUgly(2147483647)<<endl;
    return 0;
}
