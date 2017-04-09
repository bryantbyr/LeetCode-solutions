//Ugly Number II.cpp
//Run overtime
//@Author: Qi

#include<iostream>
using namespace std;

class Solution{
    public:
        bool isUgly(int num){
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

        int nthUglyNumber(int n){
            int count=0;
            int num=1;
            while(count<n){
                if(isUgly(num)){
                    count++;
                    if(count==n)
                        return num;
                }
                num++;
            }
        }
};

int main()
{
    Solution s;
    cout<<s.nthUglyNumber(1660)<<endl;
    return 0;
}
