//258. Add Digits.cpp
#include <iostream>
using namespace std;

//Created by bryantbyr on 20180819
//Time:O(n^2)
//Space:O(1)
//Brute Force
class Solution {
public:
    int addDigits(int num) {
        //return 1+(num-1)%9; //math method!
        int t=num;
        while(t/10!=0){
            num=t;
            t=0;
            while(num!=0){
                t+=num%10;
                num/=10;
            }
        }
        return t;
    }
};

int main()
{
    Solution s;
    cout<<s.addDigits(1010000)<<endl;
}
