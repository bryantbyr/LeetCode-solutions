#include <iostream>
#include <vector>
using namespace std;

//20170814
//借助vector,数值过大时会溢出
// class Solution {
// public:
    // int getSum(int a, int b) {
    //     if(a*b<0){
    //             vector<int> r(max(abs(a),abs(b)),0);
    //             for(int i=0;i<min(abs(a),abs(b));i++)
    //                 r.pop_back();
    //             return a+b>0?r.size():-r.size();
    //     }
    //     else{
    //         vector<int> s(abs(a),0);
    //         vector<int> t(abs(b),1);
    //         s.insert(s.end(),t.begin(),t.end());
    //         return a+b>0?s.size():-s.size();
    //     }
    // }
// };

//Learn from discuss
//20170814
//use bit manipulation
class Solution {
public:
    int getSum(int a, int b) {
        return b==0?a:getSum(a^b,a&b<<1);
    }
};

int main()
{
    Solution s;
    cout<<s.getSum(2147483647,-2147483648)<<endl;
    // vector<int> test;
    // cout<<test.max_size()<<endl;
}
