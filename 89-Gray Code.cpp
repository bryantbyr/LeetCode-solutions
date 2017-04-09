//89-Gray Code.cpp

#include<iostream>
#include<math.h>
#include<vector>
using namespace std;

//2017/03/23
//Time:O(2^N)
//Space:O(1)
//找到递推关系,从1到n依次迭代得到n比特的结果
class Solution{
public:
    vector<int> grayCode(int n)
    {
        vector<int> r={0};
        for(int i=0;i<n;i++){
            int end=r.size();
            for(int j=end-1;j>=0;j--)//对n=i,在原有数组的基础上逆序依次加2的i次方
                r.push_back(pow(2,i)+r[j]);
        }
        return r;
    }
};

int main()
{
    Solution s;
    vector<int> r;
    r=s.grayCode(3);
    for(int i=0;i<r.size();i++)
        cout<<r[i]<<endl;

    return 0;
}
