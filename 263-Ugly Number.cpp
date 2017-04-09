//Ugly Number.cpp
//Run time is 6ms in LeetCode

#include <iostream>
using namespace std;

class Solution{
    public:
        bool isUgly(int num){
            if(num<=0)
                return 0;
            if(num==1)
                return 1;
            while(num%2==0){
                num/=2;
                if(num==1)
                    return 1;
            }
            while(num%3==0){
                num/=3;
                if(num==1)
                    return 1;
            }
            while(num%5==0){
                num/=5;
                if(num==1)
                    return 1;
            }
            return 0;
        }
};

int main()
{
    Solution s;
    cout<<s.isUgly(5)<<endl;
    return 0;
}
